from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", views.RecipeListView.as_view(), name="recipe_list"),
    path(
        "category/none/", views.RecipeListView.as_view(), name="recipe_list_no_category"
    ),
    path("category/add/", views.CategoryCreateView.as_view(), name="category_add"),
    path("recipe/<int:pk>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipe/add/", views.RecipeCreateView.as_view(), name="recipe_add"),
    path("all/", views.PrintView.as_view(), name="all_recipes"),
    path("search/", views.RecipeListView.as_view(), name="search_results"),
]
