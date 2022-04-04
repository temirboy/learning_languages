from django import forms
from .models import VideoUrl


class AddVideoYoutube(forms.ModelForm):
    class Meta:
        model = VideoUrl
        fields = ('name', 'url')
