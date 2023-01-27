from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

from .models import Pencraft, Chapter
from Recommendation.models import PlatformUser

@login_required(redirect_field_name='login')
def index(request):
    pencraft_list = Pencraft.objects.order_by('-pub_date')
    return render(request, 'Writing/index.html', locals())

@login_required(redirect_field_name='login')
def pencraft(request, pencraft_id):
    pencraft = get_object_or_404(Pencraft, pk=pencraft_id)
    chapter_set = Chapter.objects.filter(collection=pencraft)
    return render(request, 'Writing/pencraft.html', locals())

@login_required(redirect_field_name='login')
def chapter(request, pencraft_id, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'Writing/chapter.html', locals())

@login_required(redirect_field_name='login')
def author(request, username):
    user = User.objects.get(username=username)
    platform_user = PlatformUser.objects.get(uid=user)
    pencraft_list = Pencraft.objects.filter(author=platform_user)
    return render(request, 'Writing/author.html', locals())

