
from django.contrib import admin
from django.urls import path
from index.views import html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',html)
]
