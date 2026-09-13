from django.urls import path
from register import views
urlpatterns = [
    path('register/', views.register),
    path('manage/', views.manage),
path('edit/<int:idd>', views.edit),
path('user/', views.manage_reg),
path('reject/<int:idd>', views.reject),
]