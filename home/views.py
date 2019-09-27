from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
   return render(request, 'pages/home.html')
def contact(request):
   return render(request, 'pages/contact.html')
def error(request):
   return render(request, 'pages/error.html')
def register(request):
   form = RegistrationForm()
   if request.method == 'POST':
         form= RegistrationForm(request.POST)
         if form.is_valid():
               form.save()
               return HttpResponseRedirect('/')

   return render(request, 'pages/register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "pages/login.html",
                    context={"form":form})
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
