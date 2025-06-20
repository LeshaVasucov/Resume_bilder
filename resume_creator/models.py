from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Skills_description(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

class Resume(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    description = models.TextField()
    pict = models.ImageField(upload_to="resumes/" ,blank=True)
    skills = models.ManyToManyField(Skills_description, related_name="skills")

    def __str__(self):
        return f"{self.creator}"

class ResumeFile(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)
    file = models.FilePathField()