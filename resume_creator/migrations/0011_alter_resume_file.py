# Generated by Django 5.2.1 on 2025-07-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_creator', '0010_alter_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
