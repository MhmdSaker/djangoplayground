from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def records(request):
    return HttpResponse("HELLO FROM RECORDS! ازيك ياكبير")

