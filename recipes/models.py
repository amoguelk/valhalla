from django.db import models
from django.core.validators import MinLengthValidator
from django_jsonform.models.fields import ArrayField

"""
Model to store recipe categories ("Desserts", "Soups", etc.)
"""


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, "El nombre debe ser de más de dos caracteres")
        ],
        verbose_name="Nombre",
    )
    order = models.IntegerField(default=0, verbose_name="Orden personalizado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["order"]

    def __str__(self):
        return self.name


"""
Model to store recipes
"""


class Recipe(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, "El nombre debe ser de más de dos caracteres")
        ],
        verbose_name="Título",
    )
    ingredients = ArrayField(
        base_field=models.CharField(max_length=200),
        blank=True,
        null=True,
        verbose_name="Ingredientes",
    )
    body = models.TextField(blank=True, null=True, verbose_name="Cuerpo")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Categoría",
    )
    related_recipes = models.ManyToManyField(
        "self",
        related_name="referenced_by",
        symmetrical=False,
        blank=True,
        verbose_name="Recetas relacionadas",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        ordering=["title"]

    def __str__(self):
        return self.title
