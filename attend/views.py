from django.shortcuts import render

# Create your views here.
def attend(request):
    return render(request,'attend/attend.html')