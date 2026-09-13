from django.shortcuts import render
from .models import Organizationregister
from login.models import Login
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

from organizationregister.models import Organizationregister
from login.models import Login

def organizationregister(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        # Check Organization table
        if Organizationregister.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('/organizationregister/add/')

        # Check Login table
        if Login.objects.filter(username=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('/organizationregister/add/')

        obj = Organizationregister()
        obj.email = email
        obj.username = request.POST.get('org_name')
        obj.password = request.POST.get('password')
        obj.status = 'Accepted'
        obj.save()

        ob = Login()
        ob.username = obj.email
        ob.password = obj.password
        ob.type = 'org'
        ob.u_id = obj.organization_id
        ob.save()

        messages.success(request, "Organization Registered Successfully!")
        return redirect('/')

    return render(
        request,
        'organizationregister/organizationregister.html'
    )
def manage_organization(request):
    obj = Organizationregister.objects.all()
    context = {'ok': obj}
    return render(request,'organizationregister/manage organization.html',context)

def reject(request,idd):
    ob = Organizationregister.objects.get(organization_id=idd)
    ob.status='Rejected'
    ob.save()
    return manage_organization(request)





