from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("welcome")

def demo1(request,a):
    # a=input('enter an item : ')
    return HttpResponse(a)

def q1(request,a,b):
    if b>5:
        c=0.05*a
        return HttpResponse(c)
    else:
        return HttpResponse('no change')

def q2(request,a):
    if a=='delhi':
        return HttpResponse('Redfort')
    elif a=='agra':
        return HttpResponse('Tajmahal')
    elif a=='kerala':
        return HttpResponse('varkala')
    else:
        return HttpResponse('invalid')

def q3(request,a):
    b=a%10
    if b%3==0:
        return HttpResponse('true')
    else:
        return HttpResponse('false')
    
def q4(request,a):
    if a==1:
        return HttpResponse('Sunday')
    elif a==2:
        return HttpResponse('monday')
    elif a==3:
        return HttpResponse('Tuesday')
    elif a==4:
        return HttpResponse('wednesday')
    elif a==5:
        return HttpResponse('Thursday')
    elif a==6:
        return HttpResponse('Friday')
    elif a==7:
        return HttpResponse('saturday')
    else:
        return HttpResponse('invalid')
    
def q5(request,a):
    if a>100000:
        b=a*15/100
        total=a+b
        return HttpResponse(total)
    elif a>50000 and a<=100000:
        b=a*10/100
        total=a+b
        return HttpResponse(total)
    else:
        b=a*5/100
        total=a+b
        return HttpResponse(total)
    
def q6(request,a):
    if a<100:
        return HttpResponse("Your unit price = 0")
    else:
        if a<200 and a>100:
            up=a-100
            ua=up*5
            return HttpResponse(ua)
        else:
            ui=a-200
            us=ui*10+500
            return HttpResponse(us)
def fun1(req):
    print('hallo')
    return HttpResponse("welcome")
def fun2(req,a,b):
    # print(type(a))
    return HttpResponse(a,b)
def demo(req):
    a={'name':'abc','age':22},{'name':'bbb','age':22},{'name':'ccc','age':23}
    return render(req,'demo.html',{'data':a})

users=[{'id':'21','name':'abc','age':22,'email':'abc@gmail'},{'id':'22','name':'bbb','age':23,'email':'bbb@email'},{'id':'23','name':'ccc','age':23,'email':'ccc@email'}]

def display(req):
    return render(req,'display_user.html',{'users':users})

def user_reg(req):
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']
        users.append({'id':id,'name':name,'age':age,'email':email})
        return redirect(display)
    else:
        print(req.method)
        return redirect(display)
def edit_user(req,id):
    user=""
    for i in users:
        if i ['id']==id:
            user=i
    if req.method=='POST':
        id=req.POST['id']
        name=req.POST['name']
        age=req.POST['age']
        email=req.POST['email']  
        user['id']=id
        user['name']=name
        user['age']=age
        user['email']=email
        return redirect(display) 
    return render(req,'edit_user.html',{'user':user})

def delete_user(req,id):
    for i in users:
        if i ['id']==id:
            users.remove(i)
    return redirect(display)      