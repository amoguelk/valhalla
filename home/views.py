from django.shortcuts import render


def home(request):
    return render(
        request,
        "home/homepage.html",
        {
            "pages": [
                {"url": "senshi/", "name": "Mis recetas"},
                {"url": "mithrun/", "name": "Administrar el sitio"},
            ],
            "headerText": "Bienvenidos",
        },
    )

def error_404(request, exception):
    return render(request, 'home/error_404.html', status=404)

def error_500(request):
    return render(request, 'home/error_500.html', status=500)