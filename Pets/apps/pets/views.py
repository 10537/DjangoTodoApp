from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def pets_main(request):
    return HttpResponse('Pets Main Page')
