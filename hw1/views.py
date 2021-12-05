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
# Create your views here.


def loginTask3(request):
    return render(request, 'hw1/loginTask3.html')

def registerTask1(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginTask3')

    context={'form':form}
    return render(request, 'hw1/register1.html', context)