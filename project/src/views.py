from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Create_opportunity

# 3rd party login imports
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

#jojo's imports
from src.forms import RegistrationForm, LoginForm
from src.models import Person
from django.contrib.auth import authenticate
from django.contrib.auth import login as logged
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.user.is_authenticated():
        return redirect("/home/")
    return render(request, 'login.html')

@login_required(login_url='/')
def home(request):	
    return render(request, 'home.html')
    
  
def PersonRegistration(request):
    	if request.user.is_authenticated() and not request.user.is_staff and not request.user.is_superuser:
    	    	return HttpResponseRedirect('register')

    	if request.method == 'POST':
					form = RegistrationForm(request.POST)
					if form.is_valid():
						user=User.objects.create_user(username=form.cleaned_data['username'], email= form.cleaned_data['email'], password = form.cleaned_data['password'])
						# username = uuid.uuid4();
						user.save()
						# person = Person(user=user, name=form.cleaned_data['name'])
						# person.save()
						person = Person(user=user, name=form.cleaned_data['name'])
						person.save()
						return HttpResponseRedirect('home.html')

					else:
						return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))	
    	else:
    		form = RegistrationForm()
    		context = {'form': form}
    		return render_to_response('register.html', context, context_instance=RequestContext(request))  
    		
def loginRequest(request):
	if request.user.is_authenticated() and not request.user.is_staff and not request.user.is_superuser:
		print "Section 1"
		return redirect('/register/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
				print "Section 2"
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				person = authenticate(username=username, password=password)
				if person is None:
					print "Section 3"
					logged(request, person)
					return redirect('/register/')
				else:
					print "Section 4"
					return redirect('http://127.0.0.1:8000/home/')

		else:
			print "Section 5"
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))				

	else:
		form = LoginForm()
		context = {'form': form}
		print "Section 6"
	print "Section 7"
	return render_to_response('login.html', context, context_instance=RequestContext(request))    		

def logout(request):
    auth_logout(request)
    return redirect('/')
 #Profiles
def seeker(request):	
    return render(request, 'seek.html')
    

#create opportunity form view
def create_opportunity_form(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        print form.cleaned_data.get("description")
        instance.save()
    context = {
        'form' : form
    }
    return render(request, 'create_opportunity.html', context)
    

    
    
def helper(request):	
    return render(request, 'help.html')   

def browse(request):	
    show_items = Create_opportunity.objects.order_by('-created_date')
    context = {
        'show_items': show_items
    }
    return render(request, 'browse.html', context)
   