from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include("questions.urls")),
    path("admin/", admin.site.urls),
]