from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)

    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    content.widget.attrs.update({'class': 'form-control', 'rows': 3})
