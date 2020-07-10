import os
import subprocess

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

'''
def helloView():
    return "hello world"
'''

def helloView(request, *args, **kwargs):
    result = ['hello', 'world']
    # result = {'username' : 'monkey'}
    return JsonResponse(result, safe=False)
    # return HttpResponse(result)

def helloViewBak(request, *args, **kwargs):
    htmlString = '''
    <html>
        <head>
            <title>51reboot</title>
        </head>
        <body>
            <h1>
                <font color="green">hello world</font>
            </h1>
        </body>    
    </html>
    '''
    return HttpResponse(htmlString)


def SumView(request, *args, **kwargs):
    '''
    Get
        sum = args1 + args2
        return sum
    '''
    print("request: {}".format(request))
    print("dir(request): {}".format(dir(request)))

    # print(request.method)
    # print(request.GET)
    # ?args1=1&args2=20006
    x = request.GET.get('args1')
    y = request.GET.get('args2')
    if x and y:
        print(x, y, type(x), type(y))
        s = sum([int(x), int(y)])
        print(s)
        return HttpResponse(s)
    else:
        msg = '<font color="red">args1 and args2 is required</font>'
        return HttpResponse(msg)


def CommandView(request, *args, **kwargs):
    cmd = request.GET.get('cmd')
    # result = os.system(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # print(p.returncode)
    # print(p.stdout, p.stderr)
    # print("result : {}".format(result))

    stdout, stderr = p.communicate()
    if stdout:
        result = "<pre>{}</pre>".format(stdout)
    else:
        result = stderr
    return HttpResponse(result)


def LoginShowView(request, *args, **kwargs):
    return render(request, 'login.html')


def LoginView(request, *args, **kwargs):
    '''
        登录逻辑
    '''
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username and password:
        userinfo = ('51reboot', '123456')
        if username == userinfo[0] and password == userinfo[1]:
            login_result = 'login succ'
        else:
            login_result = 'login fail'
    else:
        login_result = 'username and password is required'
    return HttpResponse(login_result)


def LoginAuthView(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username and password:
            userinfo = ('51reboot', '123456')
            if username == userinfo[0] and password == userinfo[1]:
                login_result = 'login succ'
            else:
                login_result = 'login fail'
                # return redirect('/api/login_auth/')  # 重定向 绝对路径
                return render(request, 'login.html', context={'msg' : "login fail"})
        else:
            login_result = 'username and password is required'
        return HttpResponse(login_result)

