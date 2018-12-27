from django.urls import path
from . import views

app_name = 'hobbies'

urlpatterns = [
    path('', views.who_am_i, name='who_am_i'),
    path('about', views.about_me, name='about_me'),
    path('contacts', views.contact_me, name='contact_me'),
]