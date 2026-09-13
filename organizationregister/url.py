from django.urls import path
from organizationregister import views

urlpatterns = [
    path('add/', views.organizationregister),
path('reject/<int:idd>', views.reject),

    path('manage_organization/', views.manage_organization),

]