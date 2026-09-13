from django.shortcuts import render
from .models import Securityrecommendation
# Create your views here.
def securityrecommendation(request):
    if request.method=='POST':
        obj=Securityrecommendation()
        obj.title=request.POST.get('title')
        obj.description = request.POST.get('description')
        obj.save()
    return render(request,'securityrecommendation/securityrecommendation.html')


def view(request):
    obj = Securityrecommendation.objects.all()
    context = {'ok': obj}
    return render(request,'securityrecommendation/view security actions.html',context)