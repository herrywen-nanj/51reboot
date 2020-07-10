from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.urls import reverse
from random import randint
# Create your views here.
RANDINT = randint(6666, 10000)

def index(request, **kwargs):
    if request.GET.get('randint') and  int(request.GET.get('randint')) == RANDINT: 
            return render(request, 'AdminLTE/index2.html')
    else:
        return HttpResponseRedirect(reverse('adminlte:login'))


def login(request, **kwargs):
    data = ''
    if request.method == "POST":
        print(request.POST)
        print(request.body)
        print(QueryDict(request.body).dict())
        user = request.POST.get('username')
        passwd = request.POST.get('password')
        if user == 'admin' and passwd == '123456':
            return HttpResponseRedirect(reverse('adminlte:index') + '?randint=%d' % RANDINT)
        else:
            data = "Your password or username is woring!"
    return render(request, 'AdminLTE/login.html', {'data':data})
