from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model = Post
        fields  = ('body',)