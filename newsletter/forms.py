from django import forms
from .models import Newsletter, SendMessage


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email',]


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = '__all__'
