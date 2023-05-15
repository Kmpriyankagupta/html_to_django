from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import *
# Create your views here.
def index(request):
    return render(request, 'app/signup.html')

def UserRegister(request):
    if request.method == "POST":
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = RegUser.objects.filter(Email= email)

        if user:
            message = "User Already Exist"
            return render(request, 'app/signup.html', {'msg':message})
        else:
            if password == cpassword:
                newuser = RegUser.objects.create(Username=uname, Email=email, Password=password)

                message = "User SignUp Successfully"
                return render(request, 'app/login.html', {'msg':message})
            else:
                message = "Password and Confirm password are not Matched.."
                return render(request, 'app/signup.html', {'msg':message})
            
def LoginPage(request):
    return render(request, 'app/login.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = RegUser.objects.get(Email=email,Password=password)
        if user:
            if user.Password == password:
                request.session['Username'] = user.Username
                request.session['Email'] = user.Email  

                return render(request, 'app/index.html')
            else:
                message = "Password not Match"
                return render(request,'app/login.html',{'msg':message})
            
        else:
            message = "User does not exit"
            return render(request, 'app/signup.html', {'msg':message})


'''def logout_view(request):
    return render(request,'app/logout.html')'''

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    request.session.flush()  # Clear all session data
      # Logout the user
    return render(request,'app/logout.html')
