from django.shortcuts import render
from django.http import HttpResponse,QueryDict,HttpResponseRedirect,JsonResponse
from django.urls import reverse
# Create your views here.
# def index1(request):
#     return  HttpResponse("hello")
#
#
# def index2(request):
#     year = request.GET.get('year',2019)
#     month = request.GET['month']
#     return HttpResponse("year is %s,moth is %s" % (year,month))


# def index(request,**kwargs):
#     #return HttpResponse("<p>hello World ,hello Django</p>")
#     #year = request.GET.get("year", "2019")
#     #month = request.GET["month"]
#     #return HttpResponse("year is %s,month is %s" % (year, month))
#     if request.method == "POST":
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())  #用querdict方法把body数据转换成python dict方法
#         print(type(QueryDict(request.body).dict()))
#         date = request.POST
#
#         year = date.get('year',2018) #字典方式获取，给一个默认值
#         month = date.get('month',7)
#     else:
#         print(request)
#         print(request.method)
#         print(request.META)
#         print(request.body)
#         print(kwargs)
#         year = kwargs.get('year',2018)
#         month = kwargs.get('month',7)
#     user = {'name':'reboot','age':'18'}
#     title = "devops"
#     books = ['java','python','go']
#     pople = {'name':'reboot','age':'18'}
#     products = [{'pid': 1, 'name': 'iphone'}, {'pid': 2, 'name': 'computer'}, {'pid': 3, 'name': 'TV'}]
#     return render(request,"index.html",{"pople":pople,'books':books,'title':title,'products':products})
def index(request,**kwargs):
    if request.method == 'GET':
        return render(request,'admin/index.html')


def login(request, **kwargs):
    data = ""
    if request.method == "POST":
        print(request.POST)
        print(QueryDict(request.body).dict())
        username = request.POST.get('username','reboot')
        passwd = request.POST.get('password','123456')
        if username == "admin" and passwd == "123456":
            # data = "welcome you %s" % username
            return HttpResponseRedirect(reverse("hello:index"))
            # return HttpResponseRedirect("/hello/hello/")
        else:
            data = "your passwd or username is wrong,plaeace again"
    return render(request, 'login.html', {'data':data})