from django.shortcuts import render
from . models import Register
from login.models import Login
# Create your views here.
# def register(request):
#     if request.method=='POST':
#         obj=Register()
#         obj.email=request.POST.get('email')
#         obj.username = request.POST.get('username')
#         obj.password=request.POST.get('password')
#         obj.status='Accepted'
#         obj.save()
#
#         ob=Login()
#         ob.username=obj.email
#         ob.password=obj.password
#         ob.type='user'
#         ob.u_id=obj.register_id
#         ob.save()
#     return render(request,'register/register.html')


from django.shortcuts import render, redirect
from django.contrib import messages

from register.models import Register
from login.models import Login


def register(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check email in Register table
        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('/register/register/')

        # Check email in Login table
        if Login.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('/register/register/')

        obj = Register()
        obj.email = email
        obj.username = username
        obj.password = password
        obj.status = 'Accepted'
        obj.save()

        ob = Login()
        ob.username = obj.email
        ob.password = obj.password
        ob.type = 'user'
        ob.u_id = obj.register_id
        ob.save()

        messages.success(request, "Registration Successful!")
        return redirect('/')

    return render(request, 'register/register.html')

def manage(request):
    ss=request.session['u_id']
    obj=Register.objects.filter(register_id=ss)
    context={'ok':obj}
    return render(request,'register/manage users.html',context)

from django.shortcuts import render, redirect
from django.contrib import messages

from register.models import Register
from login.models import Login

def edit(request, idd):

    obj = Register.objects.get(register_id=idd)

    if request.method == 'POST':

        email = request.POST.get('email')

        # Check if email exists for another Register user
        if Register.objects.filter(email=email).exclude(register_id=idd).exists():
            messages.error(request, "Email already exists!")
            return redirect(f'/register/edit/{idd}/')

        # Check if email exists for another Login user
        if Login.objects.filter(username=email).exclude(u_id=idd).exists():
            messages.error(request, "Email already exists!")
            return redirect(f'/register/edit/{idd}/')

        obj.email = email
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('password')
        obj.save()

        log = Login.objects.get(type='user', u_id=idd)
        log.username = obj.email
        log.password = obj.password
        log.save()

        messages.success(request, "Updated Successfully!")
        return redirect('/register/manage/')

    context = {
        'ok': obj
    }

    return render(request, 'register/update.html', context)

def manage_reg(request):
    obj=Register.objects.all()
    context={'ok':obj}
    return render(request,'register/manage user reg.html',context)

def reject(request,idd):
    ob = Register.objects.get(register_id=idd)
    ob.status='Rejected'
    ob.save()
    return manage_reg(request)

