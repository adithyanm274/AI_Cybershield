from django.urls import path
from complaint import views
urlpatterns = [
       path('complaint/',views.complaint),
       path('post_reply/<int:idd>',views.send_reply),
       path('view_complaint/',views.view_complaint),
       path('view_reply/',views.view_reply),
]