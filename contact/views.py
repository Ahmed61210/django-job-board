from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def send_massage (request):
    myinfo = Info.objects.first()

    if request.method=='POST':
        name = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail (
            name,
            message,
            email, #'from@example.com'
            [settings.EMAIL_HOST_USER], # 'to@example.com' 
        )
    
        return render(request, 'contact/contact.html', {'name': name})
    return render(request, 'contact/contact.html', {'myinfo': myinfo})
    



    
