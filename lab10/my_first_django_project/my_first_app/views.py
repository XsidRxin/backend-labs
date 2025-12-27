from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def hello_world(request):
    name = request.GET.get("name", "World")
    age = request.GET.get("age", None)
    
    if age:
        html = f"<h1>Hello, {name}! You are {age} years old.</h1>"
    else:
        html = f"<h1>Hello, {name}!</h1>"
    
    response = HttpResponse(html)
    response.set_cookie('username', name)
    return response


def hello_world_name(request, name):
    age = request.GET.get("age", None)
    
    if age:
        html = f"<h1>Hello, {name}! You are {age} years old.</h1>"
    else:
        html = f"<h1>Hello, {name}!</h1>"
    
    response = HttpResponse(html)
    response.set_cookie('username', name)
    return response


def redirect_example(request):
    return redirect("hello_world")


def json_example(request):
    data = {"name": "Bogdan", "age": 20, "city": "Moscow"}
    return JsonResponse(data)


def show_cookies(request):
    cookies = request.COOKIES
    html = "<h1>Cookies</h1><ul>"
    for key in cookies:
        html += f"<li>{key}: {cookies[key]}</li>"
    html += "</ul>"
    return HttpResponse(html)
