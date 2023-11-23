from django.db import models
from organizations.models import Organizations
from jobs.choices import JobCategories, EmployementTypes, Status, JobTypes
from base.models import Cities

class Jobdescription(models.Model):
    title = models.CharField(max_length=50)
    job_category = models.CharField(max_length=30, choices=JobCategories.choices)
    employment_type = models.CharField(max_length=30, choices=EmployementTypes.choices, default='Full-time')
    job_location = models.ForeignKey(Cities, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=20, choices=JobTypes.choices)
    mandatory_qualification = models.CharField(max_length=40)
    experience = models.IntegerField(default=0)
    description = models.TextField()
    what_we_offer = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices)
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
