from django.shortcuts import render

from django.http import HttpResponse,QueryDict,HttpResponseRedirect
from django.urls import reverse
# Create your views here.




def index(request,**kwargs):

    #title ="devops"
    #books = ['python','java','php','C++']
    #people = {'name': 'wd','age':'30','sex':'male'}

    #products = [{'pid': 1, 'name': 'iphone'}, {'pid': 2, 'name': 'computer'}, {'pid': 3, 'name': 'TV'}]

    #return render(request,'index.html',{'title':title,'books':books,'people':people,'products':products})
    return  render(request,'index2.html')

def list(request,**kwargs):
    users = [{'username':'wd','name_cn':'wd','age':18},{'username':'wd2','name_cn':'wd2','age':18},{'username':'wd3','name_cn':'wd3','age':18}]
    return render(request,'list.html',{'users':users})

def logout(request,**kwargs):
    return render(request,'login.html')

def login(request,**kwargs):
    data = ""
    if request.method == "POST":
        print(request.POST)
        print(QueryDict(request.body).dict())
        username = request.POST.get('username', 'reboot')
        passwd = request.POST.get('password', '123456')
        if username == "admin" and passwd == "123456":
            # data = "welcome you %s" % username
            #return HttpResponseRedirect(reverse("hello:index"))
            return render(request, 'index2.html',{'username':username})
            # return HttpResponseRedirect("/hello/hello/")
        else:
            data = "your passwd or username is wrong,plaeace again"
    return render(request, 'login.html', {'data': data})


# def index(request,**kwargs):
#     #print(kwargs)
#
#     #year = request.GET.get("year",'2019')
#    # print(year)
#     #month = request.GET['month']
#     #print(month)
#     #year = kwargs.get('year','2019')
#     #month = kwargs.get('month','08')
#     if request.method == 'POST':
#         print('---')
#         print(request.POST)
#         print(request.POST.get('year'))
#         print(request.POST.get('month'))
#
#         print('---')
#         data =QueryDict(request.body).dict()
#         print(data)
#         print(type(data))
#
#
#         year = data.get('year','2018')
#         month = data.get('month','07')
#
#
#     else:
#         print(request)
#         print(kwargs)
#
#         year = kwargs.get('year', '2018')
#         month = kwargs.get('month', '07')
#         data={}
#         data['year']=year
#         data['month']=month
#
#     #return HttpResponse("year is {},month is {}".format(year,month))
#     return  render(request,'index.html',{'user':data})
#     #return  HttpResponse('Hello world')