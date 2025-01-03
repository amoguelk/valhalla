from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=["created_at", "updated_at"]

class RecipeAdmin(admin.ModelAdmin):
    readonly_fields=["created_at", "updated_at"]
    list_filter=["category"]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
