from django.urls import path

from . import views

urlpatterns = [
    # ex: /discussion/
    path('', views.index, name='index'),
        # ex: /discussion/register/
    path('register/', views.GroupRegister, name='groupregister'),
    # ex: /discussion/5/
    path('<int:group_id>/', views.detail, name='detail'),
]