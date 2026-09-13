from django.shortcuts import render,redirect
from register.models import Register
from chat.models import Chat
import datetime
from django.db.models import Q
from organizationregister.models import Organizationregister
# Create your views here.
from login.models import Login


def con(request):
    ob= Organizationregister.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/viewcon.html',context)


def cochat(request, idd):
    ss = request.session.get("u_id")  # current user id
    obj = Organizationregister.objects.get(organization_id=idd)

    if request.method == 'POST':
        msg = request.POST.get('mssg')
        if msg:
            Chat.objects.create(
                message=msg,
                organization_id=idd,
                register_id=ss,
                rectype="organization",        # who is receiving? optional
                sendertype="user"        # sender
            )
        return redirect(f'/chat/con/{idd}')  # reload page after POST

    chats = Chat.objects.filter(
        Q(register_id=ss, organization_id=idd) | Q(register_id=idd, organization_id=ss)
    ).order_by('chat_id')

    context = {
        'kk': chats,
        'uu': obj,
    }

    return render(request, 'chat/chatuser1.html', context)



def std(request):
    ob=Register.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request, idd):
    ss = request.session.get("u_id")   # seller id
    obj = Register.objects.get(register_id=idd)

    if request.method == 'POST':
        msg = request.POST.get('mssg')
        if msg:
            Chat.objects.create(
                message=msg,
                register_id=idd,
                organization_id=ss,
                sendertype="organization",   # seller sending message
                rectype="user"
            )
        return redirect(f'/chat/std/{idd}')

    chats = Chat.objects.filter(
        Q(register_id=idd, organization_id=ss)
    ).order_by('chat_id')

    context = {
        'kk': chats,
        'uu': obj,
    }

    return render(request, 'chat/chatuser2.html', context)