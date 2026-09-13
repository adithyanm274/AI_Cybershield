from django.urls import path
from quiz import views

urlpatterns = [

    path('quiz/', views.quiz),
    path('view/', views.attend_quiz),
path('result/', views.quiz_result),
path('part/', views.view_participants),
path('view_quiz/', views.view_quiz),
path('edit_quiz/<int:id>/', views.edit_quiz),

]