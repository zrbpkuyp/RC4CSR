from django.contrib import admin

from .models import DiscGroup, DiscRecord

# Register your models here.

admin.site.register(DiscGroup)
admin.site.register(DiscRecord)