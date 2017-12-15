from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from vacate.models import Event

# Create your views here.
def index(request):
    return render(request,"index.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) # µÇÂ¼
            request.session['user'] = username# ½« session ÐÅÏ¢¼ÇÂ¼µ½ä¯ÀÀÆ÷
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '') # ¶ÁÈ¡ä¯ÀÀÆ÷ cookie
    return render(request,"event_manage.html",{"user":username,"events":event_list})

@login_required
def logout(request):
    auth.logout(request) #ÍË³öµÇÂ¼
    response = HttpResponseRedirect('/index/')
    return response