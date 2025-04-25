from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
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
    
def customer_record(req, pk):
    if req.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(req,"website/record.html", {'customer_record':customer_record})
    else:
        messages.success(req,"You Must Be Logged In To View That Page...")
        return redirect('home')

def customer_delete(req, pk):
    if req.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(req,"Record Deleted Siccessfully...")
        return redirect('home')
    else:
        messages.success(req,"You Must Be Logged In To Do That.....")
        return redirect('home')

def  customer_add(req):
    form=AddRecordForm(req.POST or None)
    if req.user.is_authenticated:
        if req.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(req,"Record Added...")
                return redirect('home')
        return render(req,"website/add_record.html", {'form':form})
    else:
        messages.success(req,"You Must Be Logged In To Do That.....")
        return redirect('home')