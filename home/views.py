from django.shortcuts import render


def home(request):
    return render(
        request,
        "home/homepage.html",
        {
            "pages": [{"url": "senshi/", "name": "Mis recetas"}],
            "headerText": "Bienvenidos",
        },
    )
