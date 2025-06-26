from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AttachmentCategory(models.Model):
    name = models.CharField(max_length=50)


class WorkExperience(models.Model):
    work_name = models.CharField(max_length=60)
    work_experience = models.CharField(max_length=70)
    category = models.ForeignKey(AttachmentCategory, on_delete=True, related_name="category")


EDUCATION_CHOICES = [

]

class Education(models.Model):
    education = models.CharField(max_length=50)
    category = models.ForeignKey(AttachmentCategory, on_delete=True, related_name="category")


class IndividualInfo(models.Model):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=80, blank=True)
    category = models.ForeignKey(AttachmentCategory, on_delete=True, related_name="category")


class Resume(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    description = models.TextField()
    pict = models.ImageField(upload_to="resumes/" ,blank=True)
    attachments = models.ManyToManyField(related_name="attachments")

    def __str__(self):
        return f"{self.creator}"


class ResumeFile(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)
    file = models.FilePathField()