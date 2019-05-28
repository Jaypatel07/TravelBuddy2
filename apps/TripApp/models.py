from django.db import models
from apps.LoginRegistration.models import User
from datetime import datetime, time, date
from time import strftime



class TripManager(models.Manager):
    def trip_validator(self, postData):
        d = datetime.now()
        now=d.strftime("%Y-%m-%d")
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['destination']) < 2:
            result['errors'].append("Must enter a destination of at least two characters")
        if len(postData['description']) < 10:
            result['errors'].append("Must enter a description of at least ten characters")
        if len(postData['date_from']) < 10:
            result['errors'].append("Must enter Travel Date From")
        if len(postData['date_to']) < 10:
            result['errors'].append("Must enter Travel Date To")
        if postData['date_to'] < postData['date_from']:
            result['errors'].append("Can't return earlier than you leave")
        if postData['date_from'] < now:
            result['errors'].append("Please don't enter a date in the past")
        if len(result['errors']) < 1:
            result['status'] = True
            newtrip = Trip.objects.create(
                destination=postData['destination'], start_date=postData['date_from'], 
                end_date=postData['date_to'], 
                plan=postData['description'],
                created_by=User.objects.get(id=postData['userid']))
            newtrip.trip_attendants.add(User.objects.get(id=postData['userid']))
            newtrip.save()
        return result
    def edit(self, postData):
        d = datetime.now()

        now=d.strftime("%Y-%m-%d")
       
        result = {
            'status' : False,
            'errors' : []
        }
        if len(postData['destination']) < 2:
            result['errors'].append("Must enter a destination of at least two characters")
        if len(postData['description']) < 10:
            result['errors'].append("Must enter a description of at least ten characters")
        if len(postData['date_from']) < 10:
            result['errors'].append("Must enter Travel Date From")
        if len(postData['date_to']) < 10:
            result['errors'].append("Must enter Travel Date To")
        if postData['date_to'] < postData['date_from']:
            result['errors'].append("Can't return earlier than you leave")
        if postData['date_from'] < now:
            result['errors'].append("Please don't enter a date in the past")
        if len(result['errors']) < 1:
            result['status'] = True
   
        return result

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=12)
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trip_attendants = models.ManyToManyField(User, related_name="joined_trips", null=True)
    created_by = models.ForeignKey(User, related_name="created_trips", null=True)
    
    objects = TripManager()
    
    
    # trip attendants -- > 