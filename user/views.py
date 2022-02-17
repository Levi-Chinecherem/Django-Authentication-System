from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request, 'registration/index.html')


def signup(request):
  if request.method=="POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm() 
  return render(request, 'registration/signup.html', { 'form': form })

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, "Username or Password is incorrect")
  context={}
  return render(request, 'registration/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')
