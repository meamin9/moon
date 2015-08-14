from django.shortcuts import render
from door.forms import *
from django.contrib.auth.models import User


# Create your views here.
def test_view(request):
    return register_user(request)
    # return render(request, 'common/base-with-nav.html')
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
