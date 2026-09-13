from django.shortcuts import render
from .models import Feedback
import datetime
# Create your views here.
def feedback(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Feedback()
        obj.register_id=ss
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.save()
    return render(request,'feedback/feedback.html')


def view(request):
    obj = Feedback.objects.all()
    context = {'ok': obj}
    return render(request,'feedback/view.html',context)
