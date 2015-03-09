from django.contrib import auth
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    if request.user is not None and request.user.is_active:
        return HttpResponseRedirect(reverse('main'))
    else:
        return HttpResponseRedirect(reverse('login'))

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

def forum(request):
    return HttpResponse("Forum")
