# Generated by Django 5.2.1 on 2025-06-14 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_creator', '0003_alter_resume_pict'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='text',
            new_name='description',
        ),
    ]
