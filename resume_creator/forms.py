from django import forms
from resume_creator import models
class ResumeForm(forms.ModelForm):
    class Meta():
        model = models.Resume
        fields = ["description", "pict"]


class AttachmentForm(forms.ModelForm):
    class Meta():
        model = models.Attachment
        fields = ["title", "description"]