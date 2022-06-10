from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. Welcome to python django.")


def html_view(request):
    return HttpResponse("<h1>Welcome to python django</h1>")


def html_template(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def detail(request, name):
    return HttpResponse("You're looking at student %s." % name)
