from django.conf.urls import include, url
from django.contrib import admin
import door.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'moon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', door.views.test_view),
    url(r'^register/$', door.views.register_user),
    url(r'^login/$', door.views.login_user),
    url(r'^login/success/$', door.views.login_success),
]
