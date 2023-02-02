from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pencraft_id>/', views.pencraft, name='pencraft'),
    path('<int:pencraft_id>/<int:chapter_id>/', views.chapter, name='chapter'),
    path('author/<slug:username>', views.author, name='author'),
    path('author/<slug:username>/update/', views.update, name='update'),
]