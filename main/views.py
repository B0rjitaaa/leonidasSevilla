from django.shortcuts import render
from django.core.mail import EmailMessage


def index(request):
	if request.method == 'POST':
		body = 'Nombre:  '+ request.POST.get('name') + ' ' + request.POST.get('surname') + '\n' + request.POST.get('body')
		message = EmailMessage(
			subject=request.POST.get('subject'),
			body=body, 
			from_email=request.POST.get('email'), 
			to=["chocolatesleonidassevilla@gmail.com"])
		message.send(fail_silently=False)
	return render (request, 'index.html', {})


