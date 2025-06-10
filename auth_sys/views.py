
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, template_name="auth_sys/register.html", context={ "form" : form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username , password=password)
            if user is not None :
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, message="Неправильний логін або пароль")
    else:
        form = AuthenticationForm()
    return render(request, template_name="auth_sys/login.html", context={ "form" : form})

def logout_view(request):
    logout(request)
    return redirect("login")