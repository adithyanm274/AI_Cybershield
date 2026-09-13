from django.urls import path,re_path
from chat import views

urlpatterns=[
    path('nur/',views.con),
    re_path(r'con/(?P<idd>\w+)',views.cochat),
    path('usr/',views.std),
    re_path(r'std/(?P<idd>\w+)',views.stchat),

]