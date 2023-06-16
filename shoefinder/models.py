from django.contrib import admin
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class ShoeModels(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель обуви'
        verbose_name_plural = 'Модели обуви'


class Colors(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class ShoeColors(models.Model):
    shoe = models.ForeignKey(ShoeModels, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Цвет кроссовок'
        verbose_name_plural = 'Цвета кроссовок'

    def __str__(self):
        return f"{self.shoe} - {self.color}"


class Styles(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'


class ShoeStyles(models.Model):
    shoe = models.ForeignKey(ShoeModels, on_delete=models.CASCADE)
    style = models.ForeignKey(Styles, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shoe} - {self.style}"

    class Meta:
        verbose_name = 'Стиль кроссовок'
        verbose_name_plural = 'Стили кроссовок'


class PurchaseLinks(models.Model):
    model = models.ForeignKey(ShoeModels, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    url = models.URLField()
    price = models.IntegerField()

    def __str__(self):
        return self.store_name

    @admin.display(
        boolean=True,
        ordering="price",
        description="Бюджетный вариант?",
    )
    def inexpensive(self):
        return self.price < 20000

    class Meta:
        verbose_name = 'Ссылка на покупку'
        verbose_name_plural = 'Ссылки на покупку'
