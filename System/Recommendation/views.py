from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
import datetime

from .models import Book
from Account.models import PlatformUser

@login_required(redirect_field_name='login')
def index(request):
    platform_user = PlatformUser.objects.get(uid=request.user)
    
    return render(request, 'Recommendation/index.html', locals())


@login_required(redirect_field_name='login')
def search(request):
    platform_user = PlatformUser.objects.get(uid=request.user)
    
    return render(request, 'Recommendation/search.html', locals())


@login_required(redirect_field_name='login')
def detailBook(request, book_id):
    platform_user = PlatformUser.objects.get(uid=request.user)
    book = Book.objects.get(id=book_id)
    return render(request, 'Recommendation/detailBook.html', locals())

'''
@login_required(redirect_field_name='login')
def detailTopic(request, book_id):
    platform_user = PlatformUser.objects.get(uid=request.user)
    
    return render(request, 'Recommendation/detailTopic.html', locals())
'''