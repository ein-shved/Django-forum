from django.contrib import auth
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from forum.models import Topic, Reply
from django.views import generic
from django.utils import timezone

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


class Forum(generic.ListView):
    template_name = 'forum/forum.html'
    model = Topic
    def get_queryset(self):
        return Topic.objects.order_by('-pub_date');

class TopicView(generic.DetailView):
    template_name = 'forum/topic.html'
    model = Topic

def reply(request, pk):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, pk=pk)
        if request.user.is_authenticated():
            reply = Reply(publisher=request.user,
                          topic=topic,
                          reply_text=request.POST['reply_text'],
                          pub_date = timezone.now())
            reply.save()
            return HttpResponseRedirect(reverse('topic', args=(pk,)))
        else:
            return render(request, 'forum/topic.html',
                    {'errors': 'You can not reply as guest. Please, login first',
                     'topic':topic})
    else:
        return HttpResponseRedirect(reverse('topic', args=(pk,)))


def create(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            topic = Topic(publisher=request.user,
                    topic_header=request.POST['topic_header'],
                    topic_text=request.POST['topic_text'],
                    pub_date=timezone.now())
            topic.save()
            return HttpResponseRedirect(reverse('forum'))
        else:
            return render(request, 'forum/forum.html',
                {'errors': 'You can not post as guest. Please, login first',
                 'topic_list': Topic.objects.all})
    else:
        return render(request, 'forum/create.html')
