from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def loginAuthView(request,**kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            userinfo = ('51reboot', '123456')
            role = 'Admin'
            if username == userinfo[0] and password == userinfo[1]:
                result = 'login succ.'
                return render(request, 'webpage.html',context={'user':username,'roles':role})
            else:
                result = 'login fail.'
        elif not username:
            result = 'username is required.'
        elif not password:
            result = 'password is required.'
        else:
            result = 'username and password is required.'
        return render(request,'login.html',context={'msg': result})
    else:
        return render(request,'login.html')

def webPage(request,**kwargs):
    return render(request,'webpage.html')