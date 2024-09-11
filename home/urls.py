from django.urls import path
from .views import homePage, sign_up_page, login_page, profile_page

urlpatterns = [
    path('', homePage, name='home'),
    path('signup/', sign_up_page, name='signUp'),
    path('login/', login_page, name='login'),
    path('myprofile/', profile_page, name='profile'),
]