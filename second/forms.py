from django import forms
from captcha.fields import CaptchaField
# Create your forms here.

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	subject = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea)
	captcha = CaptchaField()