from django.shortcuts import render


def home(request):
    return render(
        request,
        "recipes/home.html",
        {
            "recipes": [
                {
                    "title": "Galletas suecas de jengibre",
                    "ingredients": [
                        "Lorem ipsum dolor sit amet.",
                        "Lorem ipsum dolor sit amet.",
                        "Lorem ipsum dolor sit amet.",
                    ],
                    "body": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Molestias incidunt debitis cumque a ea eum culpa adipisci ex repellendus provident, vero quisquam minus inventore aut? Quisquam porro ratione ipsa, libero harum qui quaerat! Esse quibusdam recusandae inventore in perferendis natus.",
                }
            ]
        },
    )
