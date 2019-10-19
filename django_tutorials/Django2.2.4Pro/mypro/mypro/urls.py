"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import myfunc,myfunc1,myfunc2
from myapp1.views import form_view
from myapp.views import c_view
from myapp.views import form_view as fv
from myapp.views import form_view1 as fv1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indb/',myfunc,name='myfunc'),
    path('exp/',myfunc1,name='myfunc1'),
    path('sfiles/',myfunc2,name='myfunc2'),
    path('formv/',form_view,name='form_view'),
    path('formm/',fv,name='fv'),
    path('formn/',fv1,name='fv1'),
    path('cv/',c_view,name='c_view'),
]
