from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
path('admin/',views.admin),
path('user/',views.user),
path('org/',views.org),


]

