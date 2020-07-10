from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

# Create your views here.

def helloView(request):
    return HttpResponse("Hello World")

def sumnumber(request):
    values_list = request.GET.values()
    sum = 0
    for i in values_list:
        sum = int(i) + sum
    return HttpResponse(sum)


def usecmd(request):
    request_data = request.GET.values()
    command = list(request_data)[0]

    output = os.popen(command)
    result = output.read()
    print(type(result))

    result = '<div>' + '\n' + result + '</div>'
    return HttpResponse(result)


def auth(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    if username and password:
        userinfo = ('root', '123456')
        if username == userinfo[0] and password == userinfo[1]:
            msg = 'login succ'
        else:
            msg = 'login fail'
            return render(request, 'login.html')
    else:
        msg = 'username and password is require'
    return HttpResponse(msg)


def index(request):
    return render(request, 'login.html')


def LoginAuthView(request):
    if request.method == 'GET':
        return render(request, 'login.html', )

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            userinfo = ('root', '123456')
            if username == userinfo[0] and password == userinfo[1]:
                msg = 'login succ'
            else:
                msg = 'login fail'
                return redirect('/api/login_auth/')
        else:
            msg = 'username and password is require'
            return redirect('/api/login_auth/', message=msg)
        return HttpResponse(msg)

