from django.conf.urls import patterns, url

urlpatterns = patterns('modelsapp.views',
    url(r'^Contacts/admin/contactform/$', 'contactform', name='contactform'),
    url(r'^Contacts/admin/jobtitleform/$', 'jobtitleform', name='jobtitleform'),
    url(r'^Contacts/admin/departmentform/$', 'departmentform', name='departmentform'),
    url(r'^Contacts/admin/supervisorform/$', 'supervisorform', name='supervisorform'),
    url(r'^Contacts/admin/esearchform/$', 'esearchform', name='esearchform'),
    url(r'^Contacts/admin/editsearchform/$', 'editsearchform', name='editsearchform'),
    url(r'^Contacts/admin/deletesearchform/$', 'deletesearchform', name='deletesearchform'),
    url(r'^Contacts/adminindex/$', 'adminindex', name='adminindex'),
    url(r'^Contacts/login/', 'login',name='login'),
    url(r'^Contacts/logout/','logout',name='logout'),
    url(r'^Contacts/viewcontact/(\d+)/$','viewcontact',name='viewcontact'),
    url(r'^Contacts/editcontact/(\d+)/$','editcontactform',name='editcontactform'),
    url(r'^Contacts/deletecontact/(\d+)/$','deletecontactform',name='deletecontactform'),
    #url(r'^Contacts/logout/', 'django.contrib.auth.logout'),
)
