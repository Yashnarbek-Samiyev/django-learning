from django.shortcuts import render
from django.http import HTTPResponse

# Create your views here.

def HomePageView(request):
    return HTTPResponse("Sallom Dunyo!")
