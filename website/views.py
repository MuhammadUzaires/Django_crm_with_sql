from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
# Create your views here.
def home(req):
    records=Record.objects.all()
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        
        user=authenticate(req, username=username,password=password)
        
        if user is not None:
            login(req, user)
            messages.success(req,"You Have Been Logged In")
            return redirect('home')
        else:
            messages.success(req,"There Was An Error Logggin In, Please Try Again")
            return redirect('home')
    else:
        return render(req, 'website/home.html',{'records':records})


def logout_user(req):
    logout(req)
    messages.success(req,"You Have Logged Out......")
    return redirect('home')

def register_user(req):
    if req.method=='POST':
        form=SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(req, user)
            messages.success(req,"You Have Successfully Register....")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(req,"website/register.html", {'form':form})