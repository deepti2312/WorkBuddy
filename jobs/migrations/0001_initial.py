# Generated by Django 4.2.7 on 2023-11-23 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0002_alter_organizations_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobdescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('job_category', models.CharField(choices=[('engineering', 'Engineering'), ('hr', 'HR'), ('management', 'Management'), ('bde', 'BDE'), ('accounts', 'Accounts'), ('marketing', 'Marketing'), ('miscellaneous', 'Miscellaneous')], max_length=30)),
                ('employment_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('intern', 'Intern')], default='Full-time', max_length=30)),
                ('job_location', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('remote', 'Remote'), ('on_site', 'On-site'), ('hybrid', 'Hybrid')], max_length=20)),
                ('mandatory_qualification', models.CharField(max_length=40)),
                ('experience', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('what_we_offer', models.TextField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], max_length=20)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organizations')),
            ],
        ),
    ]
