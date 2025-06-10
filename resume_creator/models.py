from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Resume(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    text = models.TextField()
    pict = models.FileField(blank=True)

    def __str__(self):
        return f"{self.creator}"

class ResumeFile(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)
    file = models.FilePathField()