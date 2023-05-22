from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_customer(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            user.save
            user_group = Group.objects.get(name='customers') 
            user.groups.add(user_group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login_customers')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/customer_register.html', {'form': form})

def register_vendor(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            user.save
            user_group = Group.objects.get(name='vendors') 
            user.groups.add(user_group)
            username=form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}!')
            
    else:
        form = UserRegistrationForm()
    return render(request,'users/vendor_register.html', {'form':form})
