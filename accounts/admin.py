from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


admin.site.register(AdministratorProfile)
admin.site.register(CounselorProfile)