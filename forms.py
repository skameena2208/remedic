from django import forms
from .models import Contact_2,Contact_1


class ContactForm1(forms.ModelForm):
    class Meta:
        model = Contact_1
        fields = "__all__"
class ContactForm2(forms.ModelForm):
    class Meta:
        model=Contact_2
        fields="__all__"
        exclude=['status']


