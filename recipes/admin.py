from django.contrib import admin
from . import models


class RecipeIngredientInline(admin.TabularInline):
    model = models.RecipeIngredient
    extra = 0
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_filter = ["category"]
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
