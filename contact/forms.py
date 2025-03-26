from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="nombre", required=True)
    email = forms.EmailField(label="email", required=True)
    content = forms.CharField(label="contenido", required=True)