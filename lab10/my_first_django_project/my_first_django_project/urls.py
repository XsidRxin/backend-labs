from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('my_first_app.urls')),
    path('nested/', include('nested_app.urls')),
]
