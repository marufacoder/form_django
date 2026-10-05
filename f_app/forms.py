from django import forms
from f_app.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = '__all__'  # Changed 'field' to 'fields'
