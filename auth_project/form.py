from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

user = User.objects.create_user(
    'danny', 
    'dannydevito@email.com', 
    'istartedblasting'
)

user.last_name = 'devito'
user.save()