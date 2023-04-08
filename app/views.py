from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *

def Topic_insert (request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic data inserted successfully')

def Webpage_insert(request):
    tn=input('enter tn')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=tn,url=url)[0]
    WO.save()
    return HttpResponse('webpage gig gig')
def AccessRecord_insert(request):
    tn=input('enter tn')
    n=input('enter name')
    author=input('enter author')
    url=input('enter url')
    date=input('enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=AccessRecord.objects.get_or_create(topic_name=TO,name=tn,url=url,author=author,date=date)[0]
    WO.save()
    return HttpResponse('AccessRecord gig gig')
