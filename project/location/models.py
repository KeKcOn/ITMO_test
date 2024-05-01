from django.db import models

from .constants import MAX_LENGTH_COUNTRY, MAX_LENGTH_CITY
from .validators import validate_geometry


class Capital(models.Model):
    """Модель столиц."""

    country = models.CharField('Страна', max_length=MAX_LENGTH_COUNTRY)
    city = models.CharField('Город', max_length=MAX_LENGTH_CITY)
    geometry = models.JSONField('Геометрия', validators=(validate_geometry,))

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('country', 'city',),
                name='unique_country_city'
            )
        ]
        verbose_name = 'Столица'
        verbose_name_plural = 'Столицы'
        ordering = ('country',)
