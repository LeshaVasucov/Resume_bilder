from django import forms
from resume_creator import models
class ResumeForm(forms.ModelForm):
    class Meta():
        model = models.Resume
        fields = ["text", "pict"]