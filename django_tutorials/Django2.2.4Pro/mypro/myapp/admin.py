from django.contrib import admin

# Register your models here.
from myapp.models import mymodel,teacher,principal,student

admin.site.register(mymodel)
admin.site.register(teacher)
admin.site.register(principal)
admin.site.register(student)
