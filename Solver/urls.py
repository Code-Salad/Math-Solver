from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', views.upload),
    path('', views.upload.as_view(),name='upload'),
    path('process_image', views.process_image, name='process_image'),
    # path('home/', views.home),

    # path('result/', views.result),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)