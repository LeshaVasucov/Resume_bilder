# Generated by Django 5.2.1 on 2025-06-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_creator', '0002_alter_resume_pict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='pict',
            field=models.FileField(blank=True, upload_to='resumes/'),
        ),
    ]
