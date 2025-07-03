from django import forms
from resume_creator import models

class ResumeForm(forms.ModelForm):
    class Meta():
        model = models.Resume
        fields = ["description", "pict"]


# class AttachmentForm(forms.ModelForm):
#     class Meta():
#         model = models.Attachment
#         fields = ["title", "description"]


class EducationForm(forms.ModelForm):
    class Meta():
        model = models.Attachment
        fields = ["education"]


class WorkExperienceForm(forms.ModelForm):
    class Meta():
        model = models.Attachment
        fields = ["work_name", "work_experience"]


class IndividualInfoForm(forms.ModelForm):
    class Meta():
        model = models.Attachment
        fields = ["phone_number",  "email", "address"]

class CategoryFilterForm(forms.Form):
    category = forms.ChoiceField(choices=models.CATEGORY_CHOICES, required=False, label="Категорія")