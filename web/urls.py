from .views import *
from django.urls import path

urlpatterns = [
    path('',index),
    path('login/',custom_login),
    path('dashboard/',dashboard),
    path('dashboard/category/',category),
    path('dashboard/books/',books),
    path('dashboard/borrow/',borrow),
    path('dashboard/students/',student),
]
