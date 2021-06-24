from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput())
    content = forms.CharField(label='Текст', widget=forms.Textarea())