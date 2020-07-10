from django.shortcuts import render
from django.http import HttpResponse, QueryDict, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.


# def index(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year', 2019)
#     month = kwargs.get('month', 7)
#     return HttpResponse("years is {}, month is {}".format(year, month))

def index(request, **kwargs):
    if request.method == "POST":
        print(request.method)
        print(request.body)
        print(QueryDict(request.body).dict())
        print(type(QueryDict(request.body).dict()))
        data = request.POST
        year = data.get("year")
        month = data.get("month")
    else:
        user = {'name':'reboot','age':'18', 'sex':'male'}
        title = 'devops'
        books = ['python', 'java', 'php', 'js']
        products = [{'pid': 1, 'name': 'iphone'}, {'pid': 2, 'name': 'computer'}, {'pid': 3, 'name': 'TV'}]
    # return HttpResponse("years is {}, month is {}".format(year, month))
    return  render(request, 'index.html', { 'user': user, 'title':title, 'books':books, 'products':products})

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
