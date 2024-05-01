from django import forms
from .models import Profile, Experience, Education, OCCUPATION_CHOICES, SKILLS_CHOICES, Skill
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICES, initial='developer', widget=forms.Select(attrs={'class': 'form-select'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'blank': True}))
    skills = forms.MultipleChoiceField(choices=SKILLS_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}))

    class Meta:
        model = Profile
        exclude = ['user']  # Exclude the user field from the form

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
            self.save_m2m()
        return profile

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__' 
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),  # Set the number of rows to 2
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['profile'].initial = user.profile

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Set the profile of the instance to the current user's profile
        instance.profile = self.cleaned_data.get('profile')
        if commit:
            instance.save()
        return instance

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
