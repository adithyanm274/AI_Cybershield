from django.urls import path
from credential import views

urlpatterns = [
       path('crendential/',views.email_scanner),
       path('report/',views.view_reports),
       path('monitor/', views.monitor)
]