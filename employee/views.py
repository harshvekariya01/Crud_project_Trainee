from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Employee,leave
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def userupdate(request,id):
    data = Employee.objects.get(id=id)
    print("data-----------",data)
    if request.method=="POST":
        data.first_name=request.POST['firstname']
        data.last_name=request.POST['lastname']
        data.save()
        return redirect('employee:userlist')
    else:
        return render(request,"update.html",{'data':data})


def userapplyleave(request,id):
    data = Employee.objects.get(id=id)
    if request.method=="POST":
        startdate=request.POST['startdate']
        enddate = request.POST['enddate']
        reason = request.POST['reason']
        
        data = leave(user=request.user,start_date=startdate,end_date=enddate,reason=reason)
        data.save()
        print('value---------------',leave)
        return redirect("employee:userleave")
    else:
        return render(request,"apply_leave.html",{'data':data})


def home(request):
    return render(request,"index.html")

def userlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print("user---------------",user)
        
        if user is not None:
            login(request,user) 
            messages.success(request,"login sucessfully")
            return redirect("employee:home")
        else:
            messages.warning(request,"Please Enter Email And Password")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def userregister(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        if email in ('', None) or firstname in ('', None) or lastname in ('', None) or password in ('', None):
            messages.warning(request,"Please fill data")
            return render(request,'register.html')
        else:

            data=Employee.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
            print("data-------------------------",data)
            return render(request,'login.html',{'data':data})

    else:
        return render(request,'register.html')
    
def userlist(request):  
    data=Employee.objects.all()
    value={'data':data}
    return render(request,"list.html",value)


def userdelete(request,id): 
    Employee.objects.get(id=id).delete()
    return redirect('employee:userlist')

def userleave(request):
    leavedata=leave.objects.all()
    values={'leavedata':leavedata}
    return render(request,"leave.html",values)

def userlogout(request):
    logout(request)
    return redirect('employee:home')


def usernewpassword(request):
    if request.method=="POST":
        oldpassword=request.POST['oldpassword']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if oldpassword and password and confirmpassword:
            if request.user.is_authenticated:
                user = Employee.objects.get(username = request.user.username)
                if not user.check_password(oldpassword):
                    messages.warning(request,"old password is incorrect!")
                else:
                    if password != confirmpassword:
                        messages.warning(request,"new password is not match confirm password!")
                    else:
                        user.set_password(password)
                        user.save()
                        update_session_auth_hash(request, user)
                        messages.success(request,"your password has been changed successfully")
                        return redirect('employee:home')
        else:
            messages.warning(request,"sorry,all fields are required!")
    return render(request,"new_password.html")

def usermakepassword(request,id):
    data = Employee.objects.get(id=id)
    if request.method=="POST":
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password and confirmpassword:
            if request.user.is_authenticated:
                user = Employee.objects.get(username = request.user.username)
                if password != confirmpassword:
                        messages.warning(request,"new password is not match confirm password!")
                else:
                    data=make_password(password=password)
                    data.save()
                    update_session_auth_hash(request, user)
                    messages.success(request,"your password has been changed successfully")
                    return redirect('employee:userlogin')
        else:
            messages.warning(request,"sorry,all fields are required!")
    return render(request,"make_password.html",{'data':data})