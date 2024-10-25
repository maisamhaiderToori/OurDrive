from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name = 'home'),

    path('signup/', views.signup_view, name = 'signup'),
    path('login/', views.login_view, name='login'),

]
