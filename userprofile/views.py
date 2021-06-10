from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserprofileForm

def profile_page(request):
    print(request.user)
    try:
        profile = UserProfile.objects.get(user=request.user)
    except (UserProfile.DoesNotExist,TypeError):
        return HttpResponse('404')
    return render(request,'userprofile.html',{'profile':profile})

def UserProfileRegister(request):
    form = UserprofileForm()
    if request.method == 'POST':
        form = UserprofileForm(request.POST)
        if form.is_valid():

            form.save()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect ('news')
    return render(request, 'login_page.html')