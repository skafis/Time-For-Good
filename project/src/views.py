from django.shortcuts import render
from django.http import HttpResponse

# 3rd party login imports
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

# Create your views here.
def login(request):
    context = RequestContext(request)
    return render(request, 'login.html', context)

@login_required(login_url='/')
def home(request):	
    context = RequestContext(request)
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    return redirect('/')