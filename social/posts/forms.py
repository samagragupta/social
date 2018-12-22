from django import forms
from .models import Posts

class PersonForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'body', )
