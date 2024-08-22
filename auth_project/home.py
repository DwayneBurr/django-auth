from django.http import HttpResponse


def home(request):
    request.method == 'GET'
    return HttpResponse('welcome to the home page')