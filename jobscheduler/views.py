from django.shortcuts import render,redirect
from product.models import basket,keepemail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import ListSerializer
from rest_framework import generics, mixins, status
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import schedule
import time
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime
from datetime import datetime,date


#create job

def printit(sometext):
    idd =basket.objects.all()
    values = idd.values()
    # print ("values : ", str(values))
    # print(len(values))
    item=1
    for item in range(len(values)):
        now = datetime.now()
        is_item_notexists_keepemail = keepemail.objects.filter(email = values[item]['email']).exists()
        if is_item_notexists_keepemail:
            pass
        else:
            if ((now.replace(tzinfo=None)  - values[item]['date_add'].replace(tzinfo=None) ).total_seconds() / 3600>1) :
                to_email=values[item]['email']
                message = 'test'
                # basket.email
                send_email = EmailMessage('Thank you for your shopping',message,to=[to_email])
                send_email.send()
                #create keepemail
                sentemail = keepemail.objects.create(email = values[item]['email'])
                sentemail.save()
    print (sometext)

sched = BackgroundScheduler()
sched.start()

sometext = "this is a passed message"
sched.add_job(printit, "cron", [sometext], second="*/10")

#For api
class PostList(generics.ListAPIView):
    queryset = basket.objects.all()
    serializer_class = ListSerializer
class Create(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = basket.objects.all()
    serializer_class = ListSerializer
class sendemail(generics.UpdateAPIView, mixins.DestroyModelMixin):
    serializer_class = ListSerializer
    def get_queryset(self):
             baskets=basket.objects.get(id = self.kwargs['pk'])
             mail_subject = 'Thank you for your shopping'
             message = 'test'
             to_email =baskets.email
                 # basket.email
             send_email = EmailMessage(mail_subject,message,to=[to_email])
             send_email.send()
