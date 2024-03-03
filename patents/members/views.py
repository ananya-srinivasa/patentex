from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Agent
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

# views.py
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Agent

def AgentSignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        gender = request.POST.get('gender')
        mobileno = request.POST.get('mobile')
        email = request.POST.get('email')
        patent_agent_key = request.POST.get('AgentID')
        valid_till = request.POST.get('valid')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match.')
            return redirect('agent_signup')  # Redirect to the signup page

        # Check if the email is already registered
        if Agent.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('agent_signup')

        # Create a new user (agent)
        agent = Agent.objects.create_user(
            username=uname,
            email=email,
            mobile_number=mobileno,
            patent_agent_key=patent_agent_key,
            key_valid_till=valid_till,
            gender=gender,
            password=pass1
        )

        messages.success(request, 'Account created successfully.')
        return redirect('login')  # Redirect to the login page after successful signup

    return render(request, 'agent_reg.html')



from .models import Organization  # Assuming you have a model named Organization

def OrganisationPage(request):
    if request.method == 'POST':
        orgname = request.POST.get('organization-name')
        orgtype = request.POST.get('organization-type')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone-number')
        phone_number_2 = request.POST.get('phone-number-2')
        email = request.POST.get('email')
        reg_no = request.POST.get('reg-no')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('organisation_registration')  # Redirect to the registration page

        # Create an Organization instance and save it
        organization = Organization(
            orgname=orgname,
            orgtype=orgtype,
            address=address,
            phone_number=phone_number,
            phone_number_2=phone_number_2,
            email=email,
            reg_no=reg_no,
            password=password,
        )
        organization.save()

        messages.success(request, 'Organization registered successfully.')
        return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'organisation.html')  # Assuming your registration template is named 'organisation_registration.html'

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('email')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def Createpage(request):
    if request.method == 'POST':
        button_clicked = request.POST.get('button_clicked', None)

        if button_clicked == 'organization':
            # Redirect to the organization page
            return redirect('organisation')  # Replace with the actual URL name for the organization page
        elif button_clicked == 'patent':
            # Redirect to the patent page
            return redirect('agent_reg')  # Replace with the actual URL name for the patent page

    # If not a POST request or if the button_clicked parameter is not provided, render the create.html template
    return render(request, 'create.html')
        

def LogoutPage(request):
    logout(request)
    return redirect('login')