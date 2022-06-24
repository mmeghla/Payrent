from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.models import User
from .models import infor
from django.contrib.auth import authenticate, login, logout
from .models import uploadsss

class home (ListView):
    model = uploadsss
    template_name = "index.html"
    ordering = ['-id']

def info_form (request):
      if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        room_nn=request.POST['room_nn']
        ammount=request.POST['ammount']
        month=request.POST['month']
        infor_database=infor(name=name,phone=phone,room_nn=room_nn,ammount=ammount,month_details=month)
        infor_database.save()
        messages.success (request,"Your rent is successfully paid")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def upload_form (request):
      if request.method=="POST":
        username=request.POST['username']
        name=request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        price=request.POST['price']
        details=request.POST['details']
        location=request.POST['location']
        upload_database=uploadsss(username=username,name=name,phone=phone,address=address,price=price,details=details,location=location)
        upload_database.save()
        messages.success (request,"Uploaded success")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class show_data (ListView):
    template_name = "admin.html"
    model = infor
    ordering = ['-id']
    success_url=("http://127.0.0.1:8000/info_form")

class delete (DeleteView):
    template_name = "delete.html"
    model = infor
    fields = ['name']

    success_url=("http://127.0.0.1:8000/show_data")

def upload (request):
    return render (request,"upload.html")

def signinn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")
    



