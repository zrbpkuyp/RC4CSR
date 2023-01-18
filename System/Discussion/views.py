from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import DiscGroup, DiscRecord

# Create your views here.

# @login_required(redirect_field_name="origin")
def index(request):
    latest_group_list = DiscGroup.objects.order_by('-found_time')
    context = {'latest_group_list': latest_group_list}
    return render(request, 'Discussion/index.html', context)

# @login_required(redirect_field_name="origin")
def detail(request, group_id):
    group = get_object_or_404(DiscGroup, pk=group_id)
    records = DiscRecord.objects.filter(belong_to=group)
    return render(request, 'Discussion/detail.html', {'group': group, 'records': records})