from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import create_user_form

# Create your views here.
def homePage(request):
    return render(request, 'home.html')
def sign_up_page(request):
    form = create_user_form()
    if request.method == 'POST':
        form = create_user_form(request.post)
        if form.is_valid():
            form.save()
    return render(request, 'signUp.html', {'form':form})
def login_page(request):
    return render(request, 'login.html')
def profile_page(request):
    return render(request, 'profile.html')