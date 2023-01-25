from django.contrib import admin
from .models import PlatformUser, Book

# Register your models here.
admin.site.register(PlatformUser)
admin.site.register(Book)