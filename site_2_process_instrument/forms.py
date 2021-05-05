from django import forms
from django.core import validators
from site_2_process_instrument.models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"