from django.shortcuts import render
from door.forms import *


# Create your views here.
def test_view(request):
    return render(request, 'index.html')
    # return photo_view(request)
    # return render(request, 'common/nav.html')
    # return render(request, 'picture/view.html')


def photo_view(request):
    img_list = []
    for i in xrange(13):
        img_list.append('images/album/MishimaKurune/%03d.jpg' % (i+1))
    return render(request, 'picture/photos.html', {'img_list': img_list})


def register_user(request):
    print "sdddddddddddddddddddddd=================="
    if request.method == 'POST':
        form = RegisterInfo(request.POST)
        if form.is_valid():
            print form
            return render(request, 'index.html')
        else:
            print form
    else:
        form = RegisterInfo()
    return render(request, 'register.html', {'form': form})