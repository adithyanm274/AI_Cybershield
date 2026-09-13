from django.urls import path
from datasource import views

urlpatterns = [
    path('datasource/', views.add_credential),
    path('view_datasource/', views.check_credential),
    path('threat/',views.organization_dashboard)

]