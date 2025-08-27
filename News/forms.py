
from django import forms
class EmailForm(forms.Form):
    receiver_mail = forms.EmailField(label="Enter email id" )
    subject = forms.CharField(max_length=255, label= "Enter Subject", initial="Welcome to QuickNews - Your News, Your Way!", widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email_text = forms.CharField(widget=forms. Textarea(attrs={'readonly':'readonly'}), label= "Enter Email Text", initial=(
            "Thanks for signing up for QuickNews!\n"
            "We're excited to have you on board.\n"
            "Now you're all set to stay updated with the latest headlines and breaking stories all in one place.\n"
            "Enjoy the read, \n"
            "--Team QuickNews"
        )
    )