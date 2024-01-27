from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is my Home Page")

# Create your views here.
