from django.shortcuts import render
from django.urls.base import reverse_lazy


def home(request):
    return render(
        request,
        "home/homepage.html",
        {
            "pages": [
                {"url": reverse_lazy("recipes:category_list"), "name": "Mis recetas"},
                {"url": reverse_lazy("admin:index"), "name": "Administrar el sitio"},
            ],
            "header_text": "Bienvenidos",
        },
    )


def error_404(request, exception):
    return render(request, "home/error_404.html", status=404)


def error_500(request):
    return render(request, "home/error_500.html", status=500)
