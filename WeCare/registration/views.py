from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from .models import UserDetails
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.core.mail import send_mail
import string
import random

def getregsdetails(request):
    r = {}
    r.update(csrf(request))
    return render(request,'register.html', r)

def addregsdetails(request):
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    password=request.POST.get('passwd','')
    repassword=request.POST.get('repasswd','')
    passwordregex='[a-zA-Z0-9]{6,12}'
    role=request.POST.get('role','')
    admin=False
    doctor=False
    role.islower()
    if(role=="admin"):
        admin=True
    elif(role=="doctor"):
        doctor=True
    count=0
    users=UserDetails.objects.all()
    if users is not None:
        for user in users:
            if user.emailID==email:
                count=1
                break
    if count!=1:
        if len(password)>=6 and len(password)<=12:
            if re.search(passwordregex,password):
                
                if password==repassword:
                    u = UserDetails(name=name,emailID=email,password=password,IsAdmin=admin,IsDoctor=doctor)
                    u.save()
                    
                    i={}
                    i.update(csrf(request))
                    return render(request,'register.html',{'msg5':'Registered successfully'})
                    # return HttpResponseRedirect('/registration/confirmation_mail/?receiver='+email)
                else:
                    return render(request,'register.html',{'msg2':'both password must be matched.'}) 
                    
            else:
                return render(request,'register.html',{'msg4':'password credentials are not matched'})
        else:
            return render(request,'register.html',{'msg1':'password must be between 6 to 15 characters'})
    else:
        return render(request,'register.html',{'msg5':'this user is already registered'})

# def confirmation_mail(request):
#     # sender_address="nirali2k1@gmail.com"
#     # sender_pass=""
#     receiver_address=request.GET.get('receiver','')
#     if receiver_address:
#         # message = MIMEMultipart()
#         # message['From'] = sender_address
#         # message['To'] = receiver_address
#         # message['Subject'] = 'Confirmation of registration on WeCare-HealthcareSystem'
#         # mail_content="Thank you for joining our WeCare family. You are now part of our team. Your registration is confirmed. We are glad to have you here as an expert to provide correct and proper information regarding Diseases"
#         # message.attach(MIMEText(mail_content, 'plain'))
#         # session = smtplib.SMTP('smtp.gmail.com', 587)
#         # session.starttls()
#         # session.login(sender_address, sender_pass)
#         # text = message.as_string()
#         # session.sendmail(sender_address, receiver_address, text)
#         # session.quit()
#         mail_content="Thank you for joining our WeCare family. You are now part of our team. Your registration is confirmed. We are glad to have you here as an expert to provide correct and proper information regarding Diseases"
#         send_mail(
#             'Confirmation of registration on WeCare-HealthcareSystem',
#             mail_content,
#             "niralipshah2000@gmail.com",
#             [receiver_address],
#             fail_silently=False,
#         )
#         print('Mail Sent')
#     return render(request,'registration.html',{'msg5':'registration confirmation main is sent to you'})


