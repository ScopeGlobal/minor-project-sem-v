
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import auth
from .forms import SignInForm, SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render

# razorpay imports
import razorpay
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def coin_info(request):
    return render(request, 'visualization/coin-info.html')

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


def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_YozdWOsMuM2BVO", "TTT1BipZ1IIL1ZdCuZwOMDIM"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'payment/payment.html')

@csrf_exempt
def success(request):
    return render("success")