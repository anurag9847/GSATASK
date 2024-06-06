from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse



DbHost = 'localhost'
DbPort = 27017
# Create your views here.
def index(req):
    return HttpResponse('HI from WEB')

def login(req):
    ctx={}
    return render(req, 'login.html',ctx)

def main(req):
    ctx={}
    if 'name' in req.session:
        return render(req, 'main.html',ctx)
    else:
        return HttpResponse('Session Expired , login Please')    


