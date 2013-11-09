from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crudop.views.home', name='home'),
    # url(r'^crudop/', include('crudop.foo.urls')),
    url(r'^addpublisher/', 'crud.views.add_pub_form'),
    url(r'^add_pub/', 'crud.views.add_pub'),
    url(r'^list_pub/', 'crud.views.list_pub'),
    url(r'^edit_del_op/', 'crud.views.edit_del_op'),
    url(r'^edit_save_op/', 'crud.views.edit_save_op'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
