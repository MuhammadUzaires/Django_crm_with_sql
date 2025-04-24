from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(req):
    return render(req, 'website/home.html')

def login_user(req):
    pass
def logout_user(req):
    pass