from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# import requests
# from xml.etree import ElementTree as ET
# from xml.etree.ElementTree import fromstring
# from xmljson import badgerfish as bf
# from json import dumps
# import json as simplejson
<<<<<<< HEAD
import datetime
import requests
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
from json import dumps
import json as simplejson

from django.db.models import Q
from .models import PropertyDetails, Message,ShortListedPropertyDetails
from .serializer import PropertyDetailsSerializer
from registration.models import Hubree
=======

from django.db.models import Q
from .models import Property_details
from .serializer import PropertySerializer
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5


# Create your views here.
def main(request):
<<<<<<< HEAD
	print request.POST.get('name')
	return render(request,'index1.html',{'name':request.POST.get('name')})



def show(request):
	if request.method=="POST":
		# address="2114+Bigelow+Ave"
		# citystatezip="Seattle%2C+WA"
		propert = request.POST.get('address')
		l=propert.split(',')
		address = l[0]
		citystatezip = l[1]
		url = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19lq7ppy70r_305s0&address=%s&citystatezip=%s"%(address, citystatezip)
		response = requests.get(url)
		# print(response.status_code)
		c = response.content
		d = bf.data(fromstring(c))
		my_dict = dict(d)
		my_dct = my_dict['{http://www.zillow.com/static/xsd/SearchResults.xsd}searchresults']
		dct = dict(my_dct)
		final_dct = dict(dict(dict(dct['response'])['results'])['result'])
		bedrooms = dict(final_dct['bedrooms'])
		bathrooms = dict(final_dct['bathrooms'])
		address = dict(final_dct['address'])
		final_dct = {}
		final_dct['bedrooms'] = dict(bathrooms)['$']
		final_dct['bathrooms'] = dict(bathrooms)['$']
		final_dct['city'] = dict(dict(address)['city'])['$']
		final_dct['state'] = dict(dict(address)['state'])['$']
		final_dct['street'] = dict(dict(address)['street'])['$']
		name = request.POST.get('name')
		print name
        # final_dct['zipcode'] = dict(dict(address)['zipcode'])['$']
        # print final_dct
        # return HttpResponse("success")
		# return Response(final_dct, status=status.HTTP_201_CREATED)
		return render(request,'edit_your_property.html', {'data':final_dct,'zipcode':citystatezip, 'address':l[0], 'name':name})
=======
	return render(request,'index1.html')


def show(request):
	if request.method == "POST":
		l=['novel tech','kudlu gate','banglore','karnataka',560068,10,3,12,'2000sqrt']
		return render(request,'edit_your_property.html', {'data':l})


# address="address"
# citystatezip="your zipcode"
# url = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19lq7ppy70r_305s0&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA";
# response = requests.get(url)
# print(response.status_code)
# c = response.content
# d = bf.data(fromstring(c))
# e = dumps(d)
# print e

# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def save_property(request):
# 	if request.method == "POST":
# 		property_title = request.POST.get("property_title")
# 		print request.POST.get("property_title")
# 		# obj = Property_details.objects.filter(Q(property_title=property_title))
# 		# if obj:
# 		# 	print request.POST.get("property_title")
# 		# 	return HttpResponse("this property is already exist")
#   #       else:
#         serializer = PropertySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return render(request,'my_properties.html')


>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5


def save_property(request):
	if request.method == "POST":
		prty = request.POST.get('property_title')
<<<<<<< HEAD
		o = PropertyDetails.objects.filter(property_title=prty)
		if o:
			return HttpResponse("this property is already exist")
		else:
			hubree= Hubree.objects.get(Q(name=request.POST.get('name')))	
			obj=PropertyDetails(
			userid = Hubree.objects.get(Q(name=request.POST.get('name'))),
=======
		o = Property_details.objects.filter(property_title=prty)
		if o:
			return HttpResponse("this property is already exist")
		else:	
			obj=Property_details(
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
			property_title = request.POST.get('property_title'),
			address = request.POST.get('address'),
			city = request.POST.get('city'),
			state = request.POST.get('state'),
			zip_code = request.POST.get('zip_code'),
			home_type = request.POST.get('home_type'),
			beds = request.POST.get('beds'),
			baths =request.POST.get('baths'),
			rooms = request.POST.get('rooms'),
			property_size = request.POST.get('property_size'),
<<<<<<< HEAD
			fllors = request.POST.get('floors'),
			roof = request.POST.get('roof'),
			besment = request.POST.get('basement'),
			year_built = request.POST.get('year_built'),
			description = request.POST.get('description'),
			other_features = request.POST.get('other_features'))
			obj.save()
			propert = PropertyDetails.objects.filter(Q(userid=hubree.userid))
			print len(propert)
			return render(request,'desktop.html',{'name':hubree.name,'len_p':len(propert),'propert':propert})


def msg(request):
	return render(request,'msg.html')


def save(request):
	print request.POST.get('name')
	# hubree= Hubree.objects.get(Q(name=request.POST.get('name')))
	obj= Message(
		userid = Hubree.objects.get(Q(name=request.POST.get('name'))),
		msg_from = request.POST.get('msg_from'),
		address=request.POST.get("address"),
		from_subject = request.POST.get('from_subject'),
		to_subject = request.POST.get('to_subject'),
		date_time = datetime.datetime.now())
	obj.save()
	return HttpResponse('ur msg saved')


def msg_details(request):
	hubree = Hubree.objects.filter(Q(name=request.POST.get('name')))
	msg_details = Message.objects.filter(Q(name=request.POST.get('msg_from')&Q(name=hubree.userid)))
	return render(request, 'message_details.html',{'msg': msg_details})	
=======
			description = request.POST.get('description'),
			other_features = request.POST.get('other_features'))
			obj.save()
			l = [request.POST.get('property_title'),request.POST.get('address'),request.POST.get('city'),request.POST.get('state'),request.POST.get('beds'),request.POST.get('baths'),request.POST.get('property_size')]
			return render(request,'my_properties.html',{'data':l})
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
