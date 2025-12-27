from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
    path("hello/<str:name>", views.hello_world_name, name="hello_world_name"),
    path("redirect", views.redirect_example, name="redirect_example"),
    path("json", views.json_example, name="json_example"),
    path("cookies", views.show_cookies, name="show_cookies"),
]
