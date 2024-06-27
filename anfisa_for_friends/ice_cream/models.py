from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название топинга')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Топинг'
        verbose_name_plural = 'Топинги'

    def __str__(self):
        return self.title

class Wrapper(PublishedModel):
    title = models.CharField(max_length=256,verbose_name='обертка')
    class Meta:
        verbose_name = 'Обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Мороженое')
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title
