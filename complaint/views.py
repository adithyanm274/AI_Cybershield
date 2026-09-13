from django.shortcuts import render
from .models import Complaint
import datetime
# Create your views here.
def complaint(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Complaint()
        obj.complaint=request.POST.get('complaint')
        obj.date=datetime.datetime.today()
        obj.reply='Pending'
        obj.register_id=ss
        obj.save()
    return render(request,'complaint/complaint.html')


def send_reply(request,idd):
    if request.method == 'POST':
        obj = Complaint.objects.get(complaint_id=idd)
        obj.reply = request.POST.get('reply')
        obj.save()
        return complaint(request)
    return render(request,'complaint/send reply.html')

def view_complaint(request):
    obj = Complaint.objects.all()
    context = {'ok': obj}
    return render(request,'complaint/view complaint.html',context)

def view_reply(request):
    ss=request.session['u_id']
    obj = Complaint.objects.filter(register_id=ss)
    context = {'ok': obj}
    return render(request,'complaint/view reply.html',context)