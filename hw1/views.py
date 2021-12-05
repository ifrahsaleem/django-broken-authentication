from axes.decorators import axes_dispatch
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, throttle_classes
from hw1.prevent import UserLoginRateThrottle
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_login_failed

from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@axes_dispatch
def loginTask3(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(
                request, username=username, password=password)
            print(username, password)
            if user is not None:
                print('here')
                login(request, user)
                context = {}
                return redirect('home')
            else:
                messages.info(request, 'Email OR password is incorrect')

        context = {}
        return render(request, 'hw1/loginTask3.html', context)


@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'hw1/home.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginTask3')
    
def registerTask2(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginTask3')

    context={'form':form}
    return render(request, 'hw1/register2.html', context)

class LoginUser(UserLoginRateThrottle):
    throttle_classes = [UserLoginRateThrottle]

