from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world_app_view(req):
    return HttpResponse('hello_world_app_view')
