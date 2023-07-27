from django.contrib import admin
from .models import student,super_user,superduper_user
# Register your models here.
admin.site.register(student)
admin.site.register(super_user)
admin.site.register(superduper_user)