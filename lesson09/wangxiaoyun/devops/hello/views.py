from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,QueryDict

def index(request):
    msg = '<p>Hello World,Hello, Django</p>'
    return HttpResponse(msg)

# def index2(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year',2018)
#     month = kwargs.get('month',7)
#     msg = "year is {}, month is {}".format(year,month)
#     return HttpResponse(msg)

# 关键字传参数, (?<参数名>参数类型) -- 视图中通过参数名获取值(最常用)
def index2(request, **kwargs):
    if request.method == 'POST':
        print(request)     # <WSGIRequest: POST '/hello/hello/'>
        print(request.POST.getlist)   # <bound method MultiValueDict.getlist of <QueryDict: {'year': ['2019'], 'month': ['07']}>>
        print(request.POST.getlist('year'))   # ['2019']
        print(request.method)   # POST
        print(request.body)     # b'year=2019&month=07'
        print(type(request.body))  # <class 'bytes'>
        print(QueryDict(request.body).dict())   # {'year': '2019', 'month': '07'}
        print(type(QueryDict(request.body).dict()))   # <class 'dict'>
        print(request.POST)    # <QueryDict: {'year': ['2019'], 'month': ['07']}>  获取相应信息中 post发送的信息, request.POST.getlist('id')
        print(type(request.POST))   # <class 'django.http.request.QueryDict'>
        data = request.POST
        year = data.get('year','2018')
        month = data.get('month','07')
    else:
        print(request)
        print(request.method)
        print(request.META)
        print(request.body)
        print(kwargs)
        year = kwargs.get('year','2018')
        month = kwargs.get('month','07')
    msg = 'year is {}, month is {}'.format(year,month)
    # return HttpResponse(msg)
    data = {'y': year,'m':month}
    # return render(request, 'hello.html', context=data)   #写法一
    # return render(request, 'hello.html', context={'y': year,'m':month})   #写法二
    return render(request, 'hello.html', {'info': data})   #写法三

def index3(request, **kwargs):
    if request.method =='POST':
        pass
    else:
        title = 'devops'
        bookname = ['python','java','php','web']
        product = [{'pid':'1','name': 'iphone'},{'pid':2, 'name':'computer'},{'pid':'3','name':'TV'}]
        people = {'name':'wd','age':'30','sex': 'male'}
        return render(request,'hello2.html',{'titles':title,'books':bookname,'products':product,'peo':people})
