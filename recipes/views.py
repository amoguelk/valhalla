from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from . import models


class CategoryListView(View):
    template_name = "recipes/category_list.html"

    def get(self, request):
        categories = models.Category.objects.all()
        return render(
            request,
            self.template_name,
            {
                "category_list": map(
                    lambda c: {
                        "id": c.id,
                        "name": c.name,
                        "count": models.Recipe.objects.filter(category=c).count(),
                    },
                    categories,
                ),
                "no_category_count": models.Recipe.objects.filter(
                    category=None
                ).count(),
                "headerText": "Mis recetas",
            },
        )


class RecipeListView(View):
    template_name = "recipes/recipe_list.html"

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(models.Category, id=pk)
            return render(
                request,
                self.template_name,
                {
                    "category": category,
                    "recipe_list": models.Recipe.objects.filter(category=category),
                    "headerText": category.name,
                },
            )
        if request.path == reverse("recipes:search_results"):
            search_str = request.GET.get("query", "")
            return render(
                request,
                self.template_name,
                {
                    "recipe_list": models.Recipe.objects.filter(
                        title__icontains=search_str
                    ),
                    "headerText": "Resultados",
                    "query": search_str,
                },
            )
        return render(
            request,
            self.template_name,
            {
                "recipe_list": models.Recipe.objects.filter(category=None),
                "headerText": "Sin categoría",
            },
        )


class RecipeDetailView(View):
    template_name = "recipes/recipe_detail.html"

    def get(self, request, pk):
        recipe = get_object_or_404(models.Recipe, id=pk)
        return render(
            request,
            self.template_name,
            {"recipe": recipe, "headerText": recipe.title},
        )


class PrintView(View):
    template_name = "recipes/all_recipes.html"

    def get(self, request):
        categories = models.Category.objects.all()
        return render(
            request,
            self.template_name,
            {
                "category_list": map(
                    lambda c: {
                        "id": c.id,
                        "name": c.name,
                        "recipes": models.Recipe.objects.filter(category=c),
                    },
                    categories,
                ),
                "no_category_list": models.Recipe.objects.filter(category=None),
            },
        )
