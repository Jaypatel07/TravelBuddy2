from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User


def loginreg(request):
    return render(request, "LoginRegistration/index.html")

def processingReg(request):
    response = User.objects.reg_validator(request.POST)
    if response['status'] == False:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/', messages)
    else:
        request.session['userid'] = response['userid']
        request.session['name'] = User.objects.get(id=response['userid']).name
        return redirect('/success')


def processingLog(request):
    response = User.objects.log_validator(request.POST)
    if response['status'] == False:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/', messages)
    else:
        request.session['userid'] = response['userid']
        request.session['name'] = User.objects.get(id=response['userid']).name
        return redirect('/success')


def success(request):
    if 'userid' in request.session:
        return redirect('/dashboard')
    else:
        return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')
