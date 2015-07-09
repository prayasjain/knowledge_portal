from django.shortcuts import render
from login.forms import loginform
# Create your views here.


def login(request) :





    return render(request,'login/login.html',{})



def register(request) :
        registered = False


        if(request.method=='GET') :
        
            user_form = loginform()



            return render(request,'login/register.html',{'form':user_form,'registered':registered,'slug':''})
