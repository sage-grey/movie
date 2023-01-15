from django import forms
from .models import movie_details


class MovieForm(forms.ModelForm):
    class Meta:
        model=movie_details
        fields= ['name','des','year','img']