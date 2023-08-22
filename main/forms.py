from django import forms
from .models import Location, Feature, Season
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'image',
            'l_name',
            'l_tagline',
            'l_description',
            'l_summery',
            'tags'
        ]
        widgets = {
            'l_name' : forms.TextInput(attrs={"class": "form-control"}),
            'l_tagline' : forms.TextInput(attrs={"class": "form-control"}),
            'l_summery' : forms.Textarea(attrs={"class": "form-control"}),
            'l_description' : forms.Textarea(attrs={"class": "form-control"}),
            'tags' : forms.TextInput(attrs={"class": "form-control", "data-role":"tagsinput",
                        "placeholder":"A comma-separated list of tags"}),
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = [
            'sf_title',
            'sf_description',
        ]

        widgets = {
            'sf_title' : forms.TextInput(attrs={"class": "form-control"}),
            'sf_description' : forms.Textarea(attrs={"class": "form-control"}),
        }

class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = [
            's_tagline',
            's_name',
            's_description',
        ]

        widgets = {
            's_tagline' : forms.TextInput(attrs={"class": "form-control"}),
            's_name' : forms.TextInput(attrs={"class": "form-control"}),
            's_description' : forms.Textarea(attrs={"class": "form-control"}),
        }
