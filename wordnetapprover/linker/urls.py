from django.urls import path

from . import views

urlpatterns = [
    path('link', views.link, name='link'),
    path('rate/<str:s1id>/<str:s2id>/<int:rating>', views.rate_link, name='rate'),
    path('upload', views.upload_file, name="upload")
]