from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(req):
    print('hallo')
    return HttpResponse("welcome")
def fun2(req,a,b):
    # print(type(a))
    return HttpResponse(a,b)

def tnum(req,num):
    a=num%10
    if a==0:
        return HttpResponse("not divisible by 3")
    elif a%3==0:
        return HttpResponse("divisible by 3")
    else:
        return HttpResponse("not divisible by 3")
