from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.postgres.fields import ArrayField

"""
Model to store recipe categories ("Desserts", "Soups", etc.)
"""
class Category(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "El nombre debe ser de más de dos caracteres")],
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

"""
Model to store recipes
"""
class Recipe(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "El nombre debe ser de más de dos caracteres")],
    )
    body = models.TextField()
    ingredients = ArrayField(base_field=models.CharField(max_length=200))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"

    def __str__(self):
        return self.title
