from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from page.models import Requests
from django.core.paginator import Paginator

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Пользователь не существует')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Пользователь с таким логином уже зарегистрирован')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Пользователь с такой почтой уже зарегистрирован')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.warning(request, 'Пароли не совпадают')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def mypage(request):
    current_user = request.user
    apps = Requests.objects.filter(Email=current_user.email)
    paginator = Paginator(apps, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        return render(request, "mypage.html", {'apps': apps, 'page_obj': page_obj})
    else:
        return redirect('/')

def DeleteReq(request):
    abc_id = request.POST['appointment-id']
    Requests.objects.filter(id=abc_id).delete()
    return redirect('mypage')