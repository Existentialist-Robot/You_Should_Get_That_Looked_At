# -*- coding: utf-8 -*-
from django import forms
from . import models

# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = models.Search
#         fields = ['name','from_email','subject','message','receive_newsletter']

class Upload(forms.ModelForm):
    class Meta:
        model = models.Upload
        fields = ['title','body','slug','thumb','tags']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
