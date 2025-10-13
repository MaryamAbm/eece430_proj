from django.urls import path
from . import views

urlpatterns = [
    path("", views.video_list, name="video_list"),
    path("add/", views.video_create, name="video_add"),
    path("<int:pk>/", views.video_detail, name="video_detail"),
    path("<int:pk>/edit/", views.video_update, name="video_edit"),
    path("<int:pk>/delete/", views.video_delete, name="video_delete"),
]
