from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import My_User

# Create your views here.

def hello(request):
    return HttpResponse("<em>Hello everyone!, this is my first django project...</em>")

def help(request):
    diction = {"pls_add_me": "Hello, its an Employee Interests Survey form"}
    return render(request, 'myApp/assignment.html', context=diction)


def users(request):
    user_li = My_User.objects.order_by('First_Name')
    print(user_li)
    user_dict = {'users':user_li}
    return render(request,'myApp/users.html',context=user_dict)