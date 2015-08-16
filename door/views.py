from django.shortcuts import render
from door.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


def test_view(request):
    return render(request, 'bbs/test.html')
    # return render(request, 'index.html')
    # return photo_view(request)
    # return render(request, 'common/nav.html')
    # return render(request, 'picture/view.html')


def photo_view(request):
    img_list = []
    for i in xrange(13):
        img_list.append('images/album/MishimaKurune/%03d.jpg' % (i+1))
    return render(request, 'picture/photos.html', {'img_list': img_list})


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            return render(request, 'index.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    incorrect = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/login/success/')
            else:
                incorrect = True
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'incorrect': incorrect})


def login_success(request):
    return render(request, 'common/success.html')


def home(request):
    return render(request, 'home/home.html')
