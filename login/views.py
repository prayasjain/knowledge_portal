from django.shortcuts import render
from login.forms import loginform
from login.forms import account_loginform
from login.models import UserProfile
# Create your views here.


def login(request) :
    login_success=False
    if request.method == 'GET':
        login_form = account_loginform()
    elif request.method == 'POST':
        login_form = account_loginform(data=request.POST)
        try:
            l = UserProfile.objects.get(username=login_form.data['username'],password=login_form.data['password'])
            login_success=True
            return render(request,'login/login.html',{'login_form':login_form,'success':login_success,'name':l.username})

        except UserProfile.DoesNotExist :
            return render(request,'login/login.html',{'login_form':login_form,'success':login_success})






    return render(request,'login/login.html',{'login_form':login_form,'success':login_success})



def register(request) :
        registered = False

        if (request.method=='POST') :
            user_form = loginform(data=request.POST)
            if user_form.is_valid() :
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                registered=True
            else :
                print user_form.errors
            return render(request,'login/register.html',{'form':user_form,'registered':registered,'slug':''})


        if(request.method=='GET') :
        
            user_form = loginform()



            return render(request,'login/register.html',{'form':user_form,'registered':registered,'slug':''})

        return "Hello World"

