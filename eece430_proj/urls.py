from django.urls import path, include

urlpatterns = [
    path("videos/", include("videos.urls")),
]
