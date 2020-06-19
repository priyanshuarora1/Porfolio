from django.shortcuts import render
from .models import projects,cert
from django.http import HttpResponse
import smtplib, ssl
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def home(request):
    pro=projects.objects.all()[::-1]
    cer=cert.objects.all()[::-1]
    return render(request,'index.html',{'pro':pro, 'cer':cer})
def contactme(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mail=request.POST.get('email')
        subjects=request.POST.get("subject")
        message=request.POST.get("message")
        print(name,mail,subject,message)
        subject = 'Recieved Contact me from Website'
        messages = "Name:"+name+"\n"+"From:"+mail+"\n"+"Subject"+subjects+"\n"+message
        recepient ='arorapriyanshu.official@gmail.com'
        send_mail(subject,
            messages, EMAIL_HOST_USER, [recepient])
        return HttpResponse("Your message has been sent.")
def LMS(request):
    return render(request,'LMS.html')
def cal(request):
    return render(request,'cal.html')
def rps(request):
    return render(request,'rps.html')
