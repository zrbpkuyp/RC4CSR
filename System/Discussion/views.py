from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
import datetime

from Recommendation.models import PlatformUser, Book, PlatformUserManager

from .models import DiscGroup, DiscRecord

# Create your views here.

@login_required(redirect_field_name="login")
def index(request):
    latest_group_list = DiscGroup.objects.order_by('-found_time')
    context = {'latest_group_list': latest_group_list}
    return render(request, 'Discussion/index.html', context)

@login_required(redirect_field_name="login")
def detail(request: HttpRequest, group_id):
    group = get_object_or_404(DiscGroup, pk=group_id)
    records = DiscRecord.objects.filter(belong_to=group)
    
    if request.method == "POST" and request.POST:
        #TODO: likes & reply_to
        summary = request.POST["summary"]
        content = request.POST["content"]
        try:
            disc_record = DiscRecord.objects.create(
                summary=summary,
                pub_time=datetime.datetime.now(),
                publisher=PlatformUser.objects.get(uid=request.user),
                belong_to=group,
                content=content,
            )
            err_msg = "发布成功！"
        except:
            print("Something is wrong when the user discuss, uid=", request.user)
            err_msg = "操作失败，请重试！"
            return render(request, 'Discussion/detail.html', locals())

    return render(request, 'Discussion/detail.html', locals())

