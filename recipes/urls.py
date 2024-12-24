from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", views.RecipeListView.as_view(), name="recipe_list"),
]
