from django.shortcuts import render,render_to_response 
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.db.models import Q
from registration.models import HubreeUser,Hubree

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
<<<<<<< HEAD
from property.models import PropertyDetails, Message, ShortListedPropertyDetails
=======
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5

def home(request):
    return render(request,'login-signup-landing.html')

def accounts(request):
    return render(request, 'index.html')


def log_in(request):
    return render(request, 'login-form.html',{'data':''})

def main(request):
    return render(request, 'index1.html')

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
        result = Hubree.objects.filter(Q(email = email) & Q(password = password))
<<<<<<< HEAD
        # import pdb;pdb.set_trace()
        if result:
            # if result[0].name == "mahendra":
            #     hubree = Hubree.objects.all()
            #     # hubree = Hubree.objects.filter(userid=propert.values(name) )
            #     propert =PropertyDetails.objects.filter(userid__in=hubree).select_related('userid')
            #     print len(propert)
            #     return render(request, 'property-preview.html',{'len_p':len(propert),'propert':propert,'name':result[0].name})
            # #my_propeties = # Read data from properties table and send to tempalte 
            propert = PropertyDetails.objects.filter(Q(userid = result[0].userid))
            message = Message.objects.filter(Q(userid = result[0].userid))
            s_propert = ShortListedPropertyDetails.objects.filter(Q(userid=result[0].userid))
            print len(message)
            # import pdb;pdb.set_trace()
            return render(request, 'desktop.html', {'len_p':len(propert),'len_s':len(s_propert),'s_propert':s_propert,'message':message,'len_m':len(message),'name': result[0].name,'propert':propert})
=======
        if result:
            for rec in result:
                return render(request, 'my_properties.html')
                # if rec.verificationstatus:
                #     return render(request, 'index.html')
                # else:
                #     return render(request, 'signup-verification.html')
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
        else:
            return render(request, 'login-form.html', {'data':"Incorrect email address"})


def forgot(request):
    return render(request, 'reset-password.html')




@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def password(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        hubree = Hubree.objects.filter(email = email_id)
        for rec in hubree:
            rec.password = request.POST.get('password')
            rec.save()
        return render(request, 'login-form.html', {'data':'Your password is successfully changed'})
