from django.contrib import admin
from .models import Book, SearchRecord

# Register your models here.
admin.site.register(Book)
admin.site.register(SearchRecord)