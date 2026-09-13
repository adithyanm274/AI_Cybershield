from django.urls import path
from feedback import views
urlpatterns = [
       path('complaint/',views.feedback),
       path('send_reply/',views.view),

]