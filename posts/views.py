from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Bremen with Cats</h1><p>Django deployment practice</p>")