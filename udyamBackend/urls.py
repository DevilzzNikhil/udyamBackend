from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("customauth.urls")),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


