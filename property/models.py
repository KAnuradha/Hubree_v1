from django.db import models
import uuid
<<<<<<< HEAD
from registration.models import Hubree
from datetime import datetime
from django.utils import timezone
=======
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5

# Create your models here.
HOME_TYPE = (
    ('present type', 'present type'),
    ('past type', 'pasttype')
)

<<<<<<< HEAD
class PropertyDetails(models.Model):
	userid = models.ForeignKey(Hubree)
=======
class Property_details(models.Model):
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
	property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	property_title = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
<<<<<<< HEAD
	zip_code = models.CharField(max_length=15)
	home_type = models.CharField(max_length=20,choices = HOME_TYPE)
	beds = models.CharField(max_length=5)
	baths = models.CharField(max_length=5)
	rooms = models.CharField(max_length=5)
	property_size = models.CharField(max_length=20)
	fllors = models.CharField(max_length=5)
	roof = models.CharField(max_length=5)
	besment = models.CharField(max_length=5)
	year_built = models.CharField(max_length=5)
	description = models.TextField()
	other_features = models.TextField()



class Message(models.Model):
	userid = models.ForeignKey(Hubree)
	msg_from = models.CharField(max_length=50)
	address =  models.CharField(max_length=100)
	from_subject = models.TextField()
	to_subject = models.TextField()
	date_time =models.DateField(auto_now_add=True,blank=True,null=True)


class ShortListedPropertyDetails(models.Model):
	userid = models.ForeignKey(Hubree)
	property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	property_title = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=15)
	home_type = models.CharField(max_length=20,choices = HOME_TYPE)
	beds = models.CharField(max_length=5)
	baths = models.CharField(max_length=5)
	rooms = models.CharField(max_length=5)
=======
	zip_code = models.IntegerField()
	home_type = models.CharField(max_length=20,choices = HOME_TYPE)
	beds = models.IntegerField()
	baths = models.IntegerField()
	rooms = models.IntegerField()
>>>>>>> bc86e36feeb9aa6bc7ee417a87fc9f588448ded5
	property_size = models.CharField(max_length=20)
	description = models.TextField()
	other_features = models.TextField()