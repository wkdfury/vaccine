from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Slot
from django.http import HttpResponse
import random

# Create your views here.
def add(request):
    times =['12:30pm','12:00pm','11:00am','10:00am','09:00am','09:30am','10:30am','11:30am','01:00pm','01:30pm','02:30pm','03:00pm','03:30pm','04:00pm','04:30pm','04:15pm','03:15pm','12:15pm','12:45pm','02:15pm','02:45pm','01:00pm','11:15am','10:15am','10:45am','09:15am','09:45']

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        number = request.POST.get('number')
        uid = request.POST.get('uid')
        vaccine = request.POST.get('vaccine')
        dose = request.POST.get('dose')
        state = request.POST.get('state')
        district = request.POST.get('district')
        place = request.POST.get('place')
        if Slot.objects.filter(uid=uid,dose=dose).exists():
            messages.info(request,"You have already vaccinated with this dose,Please choose another one")
            return redirect('/')

        else:

            slot = Slot(name=name,uid=uid,vaccine=vaccine,dose=dose,state=state,district=district,place=place,address=address,number=number)
            slot.save()
            timer = random.randint(0,26)
            time = times[timer]
            id = Slot.objects.filter(name=name).values('id')[0]['id']

            messages.info(request,"Slot booking successfull")
            return render(request,'token.html',{'id':id,'time':time,'place':place,'name':name})
