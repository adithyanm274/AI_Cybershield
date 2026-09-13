from django.urls import path
from attend import views

urlpatterns=[

    path('attend/', views.attend),
]

