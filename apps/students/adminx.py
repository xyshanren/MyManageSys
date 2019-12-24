#from django.contrib import admin
import xadmin
from .models import *

# Register your models here.


class StudentsAdmin(object):
    list_display = ('name', 'sex', 'age', 'address',)


xadmin.site.register(Students, StudentsAdmin)
