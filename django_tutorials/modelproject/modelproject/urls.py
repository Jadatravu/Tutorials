from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'modelproject.views.home', name='home'),
    # url(r'^modelproject/', include('modelproject.foo.urls')),
    url(r'^publisher/', 'books.views.index'),
    url(r'^pub/', 'books.views.my_index'),
    url(r'^login/', 'books.views.login'),
    #url(r'^logout/', 'books.views.logout'),
    url(r'^logout/', 'django.contrib.auth.views.logout',{'next_page':'/login'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
