from django.http import HttpResponse


def nested_home(request):
    html = "<h1>Nested App Home</h1>"
    return HttpResponse(html)


def nested_about(request):
    html = "<h1>Nested About</h1><p>This is nested app</p>"
    return HttpResponse(html)


def nested_contact(request):
    html = "<h1>Nested Contact</h1><p>Email: nested@example.com</p>"
    return HttpResponse(html)
