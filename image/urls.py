from django.urls import path
from . import views

urlpatterns = [
    path("", views.GalleryView.as_view(), name="home"),
    path("upload/", views.upload_image, name="upload"),
    path("search/", views.search_images, name="search"),
    path("image/<int:pk>/", views.image_detail, name="image_detail"),
    path("image/<int:pk>/delete/", views.delete_image, name="delete"),
    path("image/<int:pk>/toggle/", views.toggle_image_status, name="toggle_status"),
    path("about/", views.about, name="about"),
]
