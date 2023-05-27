from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    parent = TreeForeignKey(
        'self',
        verbose_name=_('Родительская категория'),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    description = models.TextField(
        _('Описание'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ('name')

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Product(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    description = models.TextField(
        _('Описание'),
        null=True,
        blank=True
    )
    price = models.PositiveIntegerField(
        _('Цена'),
        default=0
    )
    quantity = models.PositiveIntegerField(
        _('Количество в наличии'),
        default=0
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_('Категория'),
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


# class OrderItem(models.Model):
#     product = models.ForeignKey(
#         Product,
#         verbose_name=_('Продукт'),
#         on_delete=models.CASCADE,
#         related_name='order_items'
#     )
#     order = models.ForeignKey(
#         'Order',
#         verbose_name=_('Заказ'),
#         on_delete=models.CASCADE,
#         related_name='order_items'
#     )
#     quantity = models.PositiveIntegerField(
#         _('Количество'),
#         default=1
#     )
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         verbose_name = _('Заказ')
#         verbose_name_plural = _('Заказы')
#         unique_together = ('product', 'order')
#
#
# class Order(models.Model):
#     name = models.CharField(
#         _('Имя'),
#         max_length=255
#     )
#     phone = models.CharField(
#         _('Телефон'),
#         max_length=255
#     )
#     email = models.EmailField(
#         _('Email'),
#         max_length=255
#     )
#     address = models.CharField(
#         _('Адрес'),
#         max_length=255
#     )
#     comment = models.TextField(
#         _('Комментарий'),
#         null=True,
#         blank=True
#     )
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = _('Заказ')
#         verbose_name_plural = _('Заказы')
#         ordering = ['-created']
#
#     def get_total_price(self):
#         return self.orderitem_set.aggregate(total=models.Sum('product__price'))['total']
#
#
# class OrderItem(models.Model):
#
#     product = models.ForeignKey(
#         Product,
#         verbose_name=_('Продукт'),
#         on_delete=models.CASCADE,
#         related_name='order_items'
#     )
#
#     order = models.ForeignKey(
#         Order,
#         verbose_name=_('Заказ'),
#         on_delete=models.CASCADE,
#         related_name='order_items'
#     )
#
#     quantity = models.PositiveIntegerField(
#         _('Количество'),
#         default=1
#     )
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         verbose_name = _('Заказ')
#         verbose_name_plural = _('Заказы')
#         unique_together = ('product', 'order')


class ProductImage(models.Model):
    image = models.URLField(
        _('Изображение')
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_('Продукт'),
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')


class Specification(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    value = models.CharField(
        _('Значение'),
        max_length=255
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_('Продукт'),
        on_delete=models.CASCADE,
        related_name='specifications'
    )

    def __str__(self):
        return f'{self.product}-{self.name}'

    class Meta:
        verbose_name = _('Спецификация')
        verbose_name_plural = _('Спецификации')

#
# class Orders:
#     def __init__(self):
#         self.products = []
#         self.specifications = []
#         self.price = 0
#         self.quantity = 0
#
#     def add_product(self, product):
#         self.products.append(product)
#         self.price += product.price
#         self.quantity += product.quantity
#
#     def add_specification(self, specification):
#         self.specifications.append(specification)
#         self.price += specification.product.price
#         self.quantity += specification.product.quantity
#
#
#     def get_total_price(self):
#         return self.price

#
# class Inventory:
#     pass
class Post:
    pass