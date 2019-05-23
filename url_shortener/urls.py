from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path('^', include('shortener_app.urls')),
    re_path('^@admin/', admin.site.urls),
]
