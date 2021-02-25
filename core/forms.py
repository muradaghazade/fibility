from django import forms
from account.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'text']

        widgets = {
            'subject': forms.TextInput(attrs={'id': 'subject', 'placeholder': 'Your Subject', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'id': 'message', 'placeholder': 'Your Message', 'class': 'form-control', 'cols':'65', 'rows': '10'}),
        }
