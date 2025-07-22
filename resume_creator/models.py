from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class AttachmentCategory(models.Model):
#     name = models.CharField(max_length=50)


# class WorkExperience(models.Model):
#     work_name = models.CharField(max_length=60)
#     work_experience = models.CharField(max_length=70)
#     category = models.ForeignKey(AttachmentCategory, on_delete=True, related_name="category")


# EDUCATION_CHOICES = [

# ]

# class Education(models.Model):
#     education = models.CharField(max_length=50)
#     category = models.ForeignKey(AttachmentCategory, on_delete=True, related_name="category")


# class IndividualInfo(models.Model):
#     phone_number = models.CharField(max_length=15, blank=True)
#     address = models.CharField(max_length=80, blank=True)
#     category = models.ForeignKey(AttachmentCategory, on_delete=True, related_name="category")
# CATEGORY_CHOICES = [
#     (' ', 'no_category'),
#     ('Education', 'education'),
#     ('Individual info', 'individual_info'),
#     ('Work experience','work_experience'),
# ]
CATEGORY_CHOICES = [
    ('no_category', ' '),
    ('education', 'Освіта'),
    ('individual_info', 'Інформація про себе'),
    ('work_experience','Досвід роботи'),
]
class Attachment(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    # IndividualInfo
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)
    # Education
    education = models.CharField(max_length=50, blank=True)
    #WorkExperience
    work_name = models.CharField(max_length=60, blank=True)
    work_experience = models.CharField(max_length=70, blank=True)


class Resume(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="creator")
    description = models.TextField()
    pict = models.ImageField(upload_to="resumes/" ,blank=True)
    attachments = models.ManyToManyField(Attachment, related_name="attachments")
    file_path = models.FilePathField(name="file_path")

    def __str__(self):
        return f"{self.creator}"

