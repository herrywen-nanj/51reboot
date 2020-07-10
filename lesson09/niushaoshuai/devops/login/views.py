from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class LoginCbv(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username','anyone')
        password = request.POST.get('password','anypass')
        if username == 'admin' and password == '123456':
            return render(request,'index.html')
        else:
            data = {'error':'用户名或密码错误！'}
            return render(request,'login.html',context=data)