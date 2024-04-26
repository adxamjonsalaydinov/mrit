from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': "col-sm-12"}),
            'email': forms.TextInput(attrs={'class': "col-sm-12"}),
            'subject': forms.TextInput(attrs={'class': "col-sm-12"}),
            'message': forms.Textarea(attrs={'class': "form-control"})
        }
