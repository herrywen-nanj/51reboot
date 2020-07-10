from django.views import View
from django.http import QueryDict, JsonResponse
from django.shortcuts import HttpResponse, render, redirect, reverse
# from django.http import QueryDict, HttpResponse
# Create your views here.

user_list = [
    {"username": "Aaron", "password": "123", "email": "aaron@1.com", "phone": "1191"},
    {"username": "Panda", "password": "123", "email": "panda@1.com", "phone": "1101"},
]


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="login.html")

    def post(self, request, *args, **kwargs):
        print("request.POST: ", request.POST)
        status = {"code": 0, "msg": "", }
        for d_user_info in user_list:
            if request.POST.get("username") == d_user_info["username"] and request.POST.get("password"):
                request.session["username"] = request.POST.get("username")
                request.session["password"] = request.POST.get("password")
                status = {"code": 0}
                break
        else:
            status["code"], status["msg"] = 1, "Username or Password error"
        print("status: ", status)
        return JsonResponse(status)


class Logout(View):
    def get(self, request, *args, **kwargs):
        print("session: ", request.session)
        print("request.session.session_key", request.session.session_key)
        print(dir(request.session))
        del request.session["username"]
        # request.session.delete(request.session.session_key)
        return redirect(reverse("hello:login"))

    def post(self, request, *args, **kwargs):
        pass


class Home(View):
    def get(self, request, *args, **kwargs):
        print(request.session)
        if not request.session.get("username", None):
            return redirect(reverse("hello:login"))

        return render(request, template_name="home.html")

    def post(self, request, *args, **kwargs):
        pass


def hello(request, *args, **kwargs):
    if request.method == "POST":
        print("POST--> args: {}\nkwargs:{}".format(args, kwargs))

        print("request.method -> ", request.method)
        print("request.POST ->", request.POST)
        print("request.META ->", request.META)
        print("request.body ->", request.body)
        # QueryDict方法将客户端传过来的二进制数据b'year=2019&month=7&year=2018' 转换为 <QueryDict: {'year': ['2019'], 'month': ['7']}>
        print(QueryDict(request.body).dict())
        return HttpResponse("POST".format(**kwargs))

    print("request.method -> ", request.method)
    print("request.GET ->", request.POST)
    print("request.META ->", request.META)
    print("request.body ->", request.body)
    # QueryDict方法将客户端传过来的二进制数据转换为 <QueryDict: {'year': ['2019'], 'month': ['7']}>
    print(QueryDict(request.body).dict())
    print("args: {}\nkwargs:{}".format(args, kwargs))
    # return HttpResponse("<span>hello </span>")

    return HttpResponse("<h1>Hello </h1><div>Today is {year} year {month} month<div/>".format(**kwargs))




