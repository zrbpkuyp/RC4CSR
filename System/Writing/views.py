from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Pencraft, Chapter


def index(request):
    pencraft_list = Pencraft.objects.order_by('-pub_date')
    context = {'pencraft_list': pencraft_list}
    return render(request, 'Writing/index.html', context)

def pencraft(request, pencraft_id):
    pencraft = get_object_or_404(Pencraft, pk=pencraft_id)
    chapter_set = Chapter.objects.filter(collection=pencraft)
    return render(request, 'Writing/pencraft.html', {'pencraft': pencraft, 'chapter_set':chapter_set})

def chapter(request, pencraft_id, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'Writing/chapter.html', {'chapter': chapter})

