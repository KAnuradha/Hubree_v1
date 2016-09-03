<<<<<<< HEAD
from .models import PropertyDetails, Message, ShortListedPropertyDetails
=======
from .models import Property_details
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
from random import random, randint
from rest_framework import serializers


<<<<<<< HEAD
class PropertyDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = PropertyDetails
		fields = ('userid','property_id','property_title','address','city','state','zip_code','home_type','beds','baths','rooms', 'property_size', 'fllors','roof','besment','year_built','description', 'other_features')



class MessageSerializer(serializers.ModelSerializer):

	class Meta:
		model = Message
		fields = ('userid', 'msg_from', 'address', 'subject', 'date_time')


class ShortListedPropertyDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = ShortListedPropertyDetails
		fields = ('userid','property_id','property_title','address','city','state','zip_code','home_type','beds','baths','rooms', 'property_size', 'description', 'other_features')


=======
class PropertySerializer(serializers.ModelSerializer):

	class Meta:
		model = Property_details
		fields = ('property_id','property_title','address','city','state','zip_code','home_type','beds','baths','rooms', 'property_size', 'description', 'other_features')
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
