# Generated by Django 5.2.1 on 2025-06-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_creator', '0006_rename_skills_description_attachment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='title',
        ),
        migrations.AddField(
            model_name='attachment',
            name='address',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='attachment',
            name='category',
            field=models.CharField(choices=[('Education', 'education'), ('Individual info', 'individual_info'), ('Work experience', 'work_experience')], default='None', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachment',
            name='education',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachment',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='attachment',
            name='work_experience',
            field=models.CharField(default='None', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachment',
            name='work_name',
            field=models.CharField(default='None', max_length=60),
            preserve_default=False,
        ),
    ]
