from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'mypro.views.home', name='home'),
    url(r'^test$', 'myapp.views.home', name='home'),
    url(r'^datatest$', 'myapp.views.data_home', name='home'),
    url(r'^ecert$', 'myapp.views.ex_cert', name='home'),

    url(r'^hello$', 'myapp.views.hello', name='home'),
    url(r'^hw$', 'mapp.views.myviewfunc', name='home'),
    url(r'^hworld$', 'mapp.views.myview_second_func', name='home'),
    url(r'^tmphworld$', 'mapp.views.my_template_view', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
