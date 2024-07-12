from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home_page(request):
    # viewa can return valid formats like html , json, xml, etc
    
    response = "<html><h1>Welcome to Myread App</html></h1>"

    # return a response
    return HttpResponse(response)

