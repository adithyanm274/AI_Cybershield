from django.urls import path
from securityrecommendation import views

urlpatterns = [

    path('securityrecommendation/', views.securityrecommendation),

    path('view/', views.view),

]

