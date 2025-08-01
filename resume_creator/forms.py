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
        widgets = {
                'education': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Освiта',
                    'required': 'required'
                }),}

class WorkExperienceForm(forms.ModelForm):
    class Meta():
        model = models.Attachment
        fields = ["work_name", "work_experience"]
        widgets = {
            'work_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва роботи',
                'required': 'required'
            }),
            'work_experience': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Досвід роботи',
                'required': 'required'
            }),}

class IndividualInfoForm(forms.ModelForm):
    class Meta():
        model = models.Attachment
        fields = ["phone_number",  "email", "address"]
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефону',
                'required': 'required'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email',
                'required': 'required'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адреса',
                'required': 'required'
            }),}
class CategoryFilterForm(forms.Form):
    category = forms.ChoiceField(choices=models.CATEGORY_CHOICES, required=False, label="Категорія", 
                                 widget=forms.Select(attrs={
            'onchange': 'this.form.submit();',
            'class': 'form-select',
            'id': "categorySelect"
        }))

