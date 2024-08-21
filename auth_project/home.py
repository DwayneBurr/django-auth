from django.http import HttpResponse


def home():
    return HttpResponse('welcome to home page')