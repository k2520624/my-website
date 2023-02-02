from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password,check_password
from .forms import  LoginForm
from .models import Fcuser



# Create your views here.

def board_detail(request, pk):
    return render(request, 'detail.html')

def home(request):
    return render(request, 'index.html')

def login_suc(request):
    return render(request, 'index1.html')

def board_list(request):
    return render(request, 'list.html')

def board_post(request):
    return render(request, 'post.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

       
        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
    


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
       

        res_data = {}

       
        if not (username and password ):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password,fcuser.password):
                request.session['user']= fcuser.id
                return render(request, 'index1.html')
            else:
                res_data['error'] = '비밀번호를 틀렸습니다'

        return render(request, 'login.html', res_data)

    
