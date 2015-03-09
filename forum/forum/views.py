from django.contrib import auth
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def index(request):
    if request.user is not None and request.user.is_active:
        return HttpResponseRedirect(reverse('forum'))
    else:
        return HttpResponseRedirect(reverse('login'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('forum'))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('forum'))
            else:
                return render(request, 'forum/login.html', {'errors': 'You are banned'})
        else:
            return render(request, 'forum/login.html', {'errors': 'Wrong login or username'})
    else:
        return render(request, 'forum/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username):
            return render(request, 'forum/register.html',
                    {'errors': 'This username is already taken'})
        user = User.objects.create_user(username=username, password=password)
        if user:
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'forum/register.html',
                    {'errors': 'Can not register user'})
    else:
        return render(request, 'forum/register.html')


def forum(request):
        return HttpResponse("Forum")
