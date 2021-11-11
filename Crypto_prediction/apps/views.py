
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import auth
from .forms import SignInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
import requests
from .models import ConsultantForm

# chart imports
from django.db.models import ObjectDoesNotExist
import json

# razorpay imports
import razorpay
from django.views.decorators.csrf import csrf_exempt

# training imports
# from Training.train_price import real_time_test, train_price

# Create your views here.


def index(request):

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    
    return render(request, 'index.html', {"data" : data})


def coin_info(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()
    return render(request, 'visualization/coin-info.html', {"data" : data})

def detailed_prediction(request):
    return render(request, 'visualization/detailed-prediction.html')

def registerPage(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/signin">signin</a>.'
            success = True
            
            return redirect("/signin/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "auth-signup.html", {"form": form, "msg" : msg, "success" : success })



def signinPage(request):
    form = SignInForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "auth-signin.html", {"form": form, "msg" : msg})


def logoutUser(request):
    auth.logout(request)
    return redirect('signin')

def profile(request, username=None):
    if User.objects.get(username=username):
        user = User.objects.get(username=username)
        return render(request,"index.html",{"user" : user})


def consultant_form(request):
    if request.method=='POST':
        form =ConsultantForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        bank_ifsc=request.POST.get('bank_ifsc')
        bank_acc_no=request.POST.get('bank_acc_no')
        exp=request.POST.get('exp')
        ins=ConsultantForm(name=name,email=email,phone_no=phone_no,bank_ifsc=bank_ifsc,bank_acc_no=bank_acc_no,exp=exp)
        ins.save()
        messages.success(request, 'Details submitted successfully')
        
        return redirect('payment')
    else:
        form = ConsultantForm()
    return render(request,'payment/consultant.html')


def payment(request):
    db_list = ConsultantForm.objects.all()
    return render(request,"payment/payment.html",{"db_list":db_list})

@csrf_exempt
def success(request):
    return render("success")


