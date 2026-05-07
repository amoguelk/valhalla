from django.core.validators import MinLengthValidator
from django.db import models
from django_jsonform.models.fields import JSONField

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
    INGREDIENTS_SCHEMA = {
        "type": "array",
        "items": {
            "oneOf": [
                {
                    "type": "object",
                    "title": "Ingrediente desglosado",
                    "properties": {
                        "name": {
                            "type": "string",
                            "title": "Nombre",
                            "required": True,
                        },
                        "main_qty": {
                            "type": "number",
                            "title": "Cantidad principal",
                            "required": False,
                            "exclusiveMinimum": 0.0,
                        },
                        "main_unit": {
                            "type": "string",
                            "title": "Unidad principal",
                            "required": False,
                        },
                        "secondary_qty": {
                            "type": "number",
                            "title": "Cantidad secundaria",
                            "required": False,
                            "exclusiveMinimum": 0.0,
                        },
                        "secondary_unit": {
                            "type": "string",
                            "title": "Unidad secundaria",
                            "required": False,
                        },
                    },
                },
                {
                    "type": "string",
                    "title": "(LEGACY) Descripción completa",
                },
            ]
        },
        "minItems": 0,
    }
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, "El nombre debe ser de más de dos caracteres")
        ],
        verbose_name="Título",
    )
    ingredients = JSONField(
        schema=INGREDIENTS_SCHEMA,
        null=True,
        blank=True,
        default=None,
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
        ordering = ["title"]

    def __str__(self):
        return self.title
