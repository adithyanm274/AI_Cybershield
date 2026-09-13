from django.shortcuts import render
from .models import Login
from django.http import HttpResponseRedirect
# Create your views here.
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get('username')
#         password = request.POST.get('password')
#         obj = Login.objects.filter(username=user_name,password=password)
#         tp = ''
#         for ob in obj:
#             tp = ob.type
#             u_id = ob.u_id
#             if tp == "admin":
#                 request.session["u_id"] = u_id
#                 return HttpResponseRedirect('/temp/admin/')
#             elif tp == "user":
#                 request.session["u_id"] = u_id
#                 return HttpResponseRedirect('/temp/user/')
#             elif tp == "org":
#                 request.session["u_id"] = u_id
#                 return HttpResponseRedirect('/temp/org/')
#         else:
#             objlist = "user_name or password incorrect"
#             context = {
#                 'm' : objlist
#             }
#             return render(request, 'login/login.html',context)
#     return render(request, 'login/login.html')


from django.shortcuts import render
from .models import Login
from django.http import HttpResponseRedirect
from register.models import Register
from organizationregister.models import Organizationregister

def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        login_obj = Login.objects.filter(
            username=user_name,
            password=password
        ).first()

        if login_obj:

            tp = login_obj.type
            u_id = login_obj.u_id

            # User Login
            if tp == "user":
                user = Register.objects.filter(register_id=u_id).first()

                if user and user.status.lower() == "rejected":
                    return render(request, 'login/login.html', {
                        'msg': 'Your account has been rejected by the administrator.'
                    })

                request.session["u_id"] = u_id
                return HttpResponseRedirect('/temp/user/')

            # Organization Login
            elif tp == "org":
                org = Organizationregister.objects.filter(
                    organization_id=u_id
                ).first()

                if org and org.status.lower() == "rejected":
                    return render(request, 'login/login.html', {
                        'msg': 'Your organization account has been rejected by the administrator.'
                    })

                request.session["u_id"] = u_id
                return HttpResponseRedirect('/temp/org/')

            # Admin Login
            elif tp == "admin":
                request.session["u_id"] = u_id
                return HttpResponseRedirect('/temp/admin/')

        return render(request, 'login/login.html', {
            'msg': 'Invalid username or password.'
        })

    return render(request, 'login/login.html')