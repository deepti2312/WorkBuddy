from django.db import models
from django.utils.translation import gettext_lazy as _


class JobCategories(models.TextChoices):
    engineering = (
        'engineering',
        _('Engineering'),
    )
    hr = 'hr', _('HR')
    management = (
        'management',
        _('Management'),
    )
    bde = (
        'bde',
        _('BDE'),
    )
    accounts = (
        'accounts',
        _('Accounts'),
    )
    marketing = (
        'marketing',
        _('Marketing'),
    )

    miscellaneous = 'miscellaneous', _('Miscellaneous')

    def getName():
        return "Job Category"


class EmployementTypes(models.TextChoices):
    full_time = (
        'full_time',
        _('Full-time'),
    )
    part_time = (
        'part_time',
        _('Part-time'),
    )
    intern = 'intern', _('Intern')

    def getName():
        return "Employment Type"


class JobTypes(models.TextChoices):
    remote = (
        'remote',
        _('Remote'),
    )
    on_site = (
        'on_site',
        _('On-site'),
    )
    hybrid = 'hybrid', _('Hybrid')

    def getName():
        return "Job Type"


class Status(models.TextChoices):
    open = (
        'open',
        _('Open'),
    )
    closed = (
        'closed',
        _('Closed'),
    )

    def getName():
        return "Status"
