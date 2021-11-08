from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from .models import Apply, Hire
from Home.models import Contact
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

#from Home.models import Login



# Create your views here.

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        loginUsername = request.POST['loginUsername']
        loginPass = request.POST['loginPass']

        user = authenticate(username = loginUsername, password= loginPass)

        if user is not None:
           login(request, user)
           messages.success(request, 'Your are successfully logged in!')
           return redirect ('home')
        else:
            messages.error(request, 'username or password does not exist')
            return redirect ('home')
    context = {'page':page}
    return render(request, 'login.html', context) 

def logoutUser(request):
    logout(request)
    messages.success(request, 'Your are logged out!')
    return redirect('home')

def signupUser(request):
    if request.method == 'POST' :
        sign_username = request.POST['sign_username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        signup_email = request.POST['signup_email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(sign_username) > 15:
            messages.error(request, 'Username must be under 15 characters')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, 'Password do not match')
            return redirect('home')

        myuser = User.objects.create_user(sign_username, signup_email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname 
        myuser.save()
        messages.success(request, 'Your are successfully signed in!')
        return redirect('home')
    return render(request, 'login.html') 

@login_required(login_url='login')
def apply(request):
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            nid = request.POST.get('nid')
            skills_have = request.POST.get('skills_have')
            skill_want = request.POST.get('skill_want')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            city = request.POST.get('city')
            zip = request.POST.get('zip')
            resume = request.POST.get('resume')
            apply = Apply(first_name=first_name, last_name=last_name, nid=nid, skills_have=skills_have, skill_want=skill_want, email=email, password=password, address=address, city=city, zip=zip, resume=resume, date = datetime.today())
            apply.save()
            messages.success(request, 'Welcome to Manpower Agency!')
            return redirect('home')
            # return redirect('home') 
        # else:
        #     messages.error(request, 'This is not valid')
        return render(request, 'apply.html') 

@login_required(login_url='login')
def hire(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        company_type = request.POST.get('company_type')
        trade_license = request.POST.get('trade_license')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        employee_recuirement = request.POST.get('employee_recuirement')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        cc_name = request.POST.get('cc_name')
        cc_number = request.POST.get('cc_number')
        cc_expiration = request.POST.get('cc_expiration')
        cc_cvv = request.POST.get('cc_cvv')
        hire = Hire(company_name=company_name, company_type=company_type, trade_license=trade_license, email=email, password=password, address=address, employee_recuirement=employee_recuirement, city=city, zip=zip, cc_name=cc_name, cc_number=cc_number, cc_expiration=cc_expiration, cc_cvv=cc_cvv, date = datetime.today())
        hire.save()
        messages.success(request, 'Welcome to Manpower Agency!')
        return redirect('home') 

    # else:
    #     messages.error(request, 'This is not valid')

    return render(request, 'hire.html') 

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
  
@login_required(login_url='login')
def jobs(request):
    return render(request, 'jobs.html') 

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html') 
    
@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('contact') 
    return render(request, 'contact.html') 
   
