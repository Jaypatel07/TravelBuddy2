
from django.shortcuts import render, HttpResponse, redirect
from ..TripApp.models import User
from .models import *
from django.contrib import messages


def index(request):
    context = {
        'trips': Trip.objects.filter(trip_attendants=request.session['userid']),
        'mytrips': Trip.objects.filter(created_by =request.session['userid']),
        'other_trips': Trip.objects.exclude(trip_attendants=request.session['userid']),
        'userid': request.session['userid'],
     
    }

    return render(request, "TripApp/travels.html", context)


def destination(request, id):
    context = {
        'trip': Trip.objects.get(id=id),
        'planner': User.objects.get(id=(Trip.objects.get(id=id).created_by_id)).name,
        'others': User.objects.filter(joined_trips=id).exclude(id=(Trip.objects.get(id=id).created_by_id)),
    }
    return render(request, "TripApp/destination.html", context)


def add(request):
    return render(request, "TripApp/add.html")


def processTrip(request):
    valid = Trip.objects.trip_validator(request.POST)
    if valid['status'] == False:
        for error in valid['errors']:
            messages.error(request, error)
        return redirect('/dashboard/add', messages)
    else:
        return redirect('/dashboard')


def join(request, id):
    trip = Trip.objects.get(id=id)
    trip.trip_attendants.add(User.objects.get(id=request.session['userid']))
    return redirect('/dashboard')


def delete(request, id):
    delete = Trip.objects.get(id=id)
    delete.delete()
    return redirect('/dashboard')


def edit(request, id):
    context = {
        'trip': Trip.objects.get(id=id),
        'planner': User.objects.get(id=(Trip.objects.get(id=id).created_by_id)).name,
        'others': User.objects.filter(joined_trips=id).exclude(id=(Trip.objects.get(id=id).created_by_id))
    }
    return render(request, "TripApp/edit.html", context)


def editTrip(request, id):
    context = {
            'trip': Trip.objects.get(id=id),
            'planner': User.objects.get(id=(Trip.objects.get(id=id).created_by_id)).name,
            'others': User.objects.filter(joined_trips=id).exclude(id=(Trip.objects.get(id=id).created_by_id))
    }
    valid = Trip.objects.edit(request.POST)
    if valid['status'] == False:
        for error in valid['errors']:
            messages.error(request, error)
        return render(request, "TripApp/edit.html", context, messages)
    else:
 
        edittrip = Trip.objects.get(id=id)
        edittrip.destination = request.POST['destination']
        edittrip.start_date = request.POST['date_from']
        edittrip.end_date = request.POST['date_to']
        edittrip.plan = request.POST['description']
        edittrip.save()
        return redirect('/dashboard', context)
    
def deletejoin(request, id):
    context = {
            'trip': Trip.objects.get(id=id),
            'planner': User.objects.get(id=(Trip.objects.get(id=id).created_by_id)).name,
            'others': User.objects.filter(joined_trips=id).exclude(id=(Trip.objects.get(id=id).created_by_id))
    }
    this_trip = Trip.objects.get(id=id)
    this_user = User.objects.get(id=request.session['userid'])
    this_trip.trip_attendants.remove(this_user)
     
    return redirect('/dashboard', context)
    

