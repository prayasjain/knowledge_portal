from django.shortcuts import render
from login.forms import loginform
# Create your views here.


def login(request) :





    return render(request,'login/login.html',{})



def register(request) :
        registered = False

        if (request.method=='POST') :
            user_form = loginform(data=request.POST)
            try :
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                registered=True
            except :
                print user_form.errors
            return render(request,'login/register.html',{'form':user_form,'registered':registered,'slug':''})


        if(request.method=='GET') :
        
            user_form = loginform()



            return render(request,'login/register.html',{'form':user_form,'registered':registered,'slug':''})

        return "Hello World"

