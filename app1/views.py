from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def king(request):
    return HttpResponse('<h1>vikings</h1>')

def vikin(request):
    return HttpResponse('<h1>king</h1>')

def king(request):
    return HttpResponse('valhalla')