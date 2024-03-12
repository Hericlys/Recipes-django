from django.shortcuts import render


def home(request) -> render:
    return render(request, "recipes/home.html")
