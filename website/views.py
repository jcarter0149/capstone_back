from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse
from .models import *
from website.forms import *

def index(request):
    template_name = 'index.html'
    sessions = Session.objects.all()
    detainees = Detainee.objects.all()
    roles = Role.objects.all()
    profiles = Profile.objects.all()
    return render(request, template_name, {'session_list': sessions, 'detainee_list': detainees, 'role_list': roles, 'profile_list': profiles})


# Create your views here.
def register(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form})


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username=request.POST['username']
        password=request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('/')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")


    return render(request, 'login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')


def addmember(request):
     # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            # registered = True

        # return render(request, 'index.html')
        return HttpResponseRedirect(reverse('website:editprofile'))

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'addmember.html'
        return render(request, template_name, {'user_form': user_form})

@login_required        
def add_detainee(request):
    if request.method == 'GET':
        detainee_form = DetaineeForm() 
        template_name = 'adddetainee.html'
        return render(request, template_name, {'detainee_form': detainee_form})  

    elif request.method == 'POST':
        form = DetaineeForm(request.POST)
        form.data = request.POST
        form.save()
        return HttpResponseRedirect('/')

@login_required
def session(request):
    if request.method == 'GET':
        session_form = SessionForm() 
        template_name = 'session.html'
        return render(request, template_name, {'session_form': session_form}) 
    
    elif request.method == 'POST':
        form = SessionForm(request.POST)
        form.data = request.POST
        form.save()
        return  HttpResponseRedirect('/')

@login_required
def report(request):
    if request.method == 'GET':
        report_form = ReportForm() 
        template_name = 'createreport.html'
        return render(request, template_name, {'report_form': report_form}) 
    
    elif request.method == 'POST':
        form = ReportForm(request.POST)
        form.data = request.POST
        form.save()
        return  HttpResponseRedirect('/')

def detainee(request, pk):
    detainee = Detainee.objects.get(pk=pk)
    reports = Report.objects.all()
    sessions = Session.objects.all()
    return render(request, 'detainee.html', {'detainee': detainee, 'reports_list': reports,'session_list': sessions})

def singlereport(request, pk):
    report = Report.objects.get(pk=pk)
    sessions = Session.objects.all()
    return render (request, 'singlereport.html', {'report': report})

class updatesessionrole(UpdateView):
    # session = Session.objects.get(pk=pk)
    model = Session
    fields = ('role',)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/')

class editreport(UpdateView):
    model = Report
    fields = ('text_data',)
    template_name = 'editreport.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('website:singlereport', kwargs={'pk':self.object.id}))
    
@login_required
def editprofile(request):
    if request.method == 'GET':
        profile_form = ProfileForm() 
        template_name = 'editprofile.html'
        return render(request, template_name, {'profile_form': profile_form}) 
    
    elif request.method == 'POST':
        form = ProfileForm(request.POST)
        form.data = request.POST
        form.save()
        return  HttpResponseRedirect('/')

