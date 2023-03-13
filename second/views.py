from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
# from django.shortcuts import render
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject'], 
			toMail = settings.EMAIL_HOST_USER
			body = {
				'name': form.cleaned_data['name'],
				'from_mail': form.cleaned_data['email_address'],   
				'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			print('subject: ==> ', subject[0])
			print('Body: ==> ', type(message))
			try:
				send_mail(subject[0], message, body['from_mail'], [toMail]) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
	form = ContactForm()
	return render(request, 'index.html', {'form':form})
