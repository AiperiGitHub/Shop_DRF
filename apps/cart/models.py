from django.db import models

from apps.shops.models import Product
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    paid = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())

# def calculate_total_price(self):
#         # Логика для вычисления общей стоимости заказа
#         # Может включать суммирование цен товаров, учет скидок и т.д.
#         # Например:
#     items = self.order_items.all()  # Получаем товары из связанной модели OrderItem
#     total_price = sum(item.price for item in items)  # Суммируем цены товаров
#     self.total_price = total_price  # Присваиваем общую стоимость заказа
#     self.save()  # Сохраняем изменения


class OrderItem(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    # quantity = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(
        default=1
    )

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


def update_inventory(self):
        # Логика для обновления инвентаря на основе заказа
        # Может включать уменьшение количества доступных товаров и т.д.
        # Например:
    items = self.order_items.all()  # Получаем товары из связанной модели OrderItem
    for item in items:
        product = item.product  # Получаем связанный товар
        product.quantity -= item.quantity  # Уменьшаем количество товара в инвентаре
        product.save()  # Сохраняем изменения

    # Другие методы и поля модели Order


class Inventory(models.Model):
    product_name = models.CharField(
        max_length=100
    )  # Название товара
    available_quantity = models.PositiveIntegerField()  # Количество доступных товаров
    sold_quantity = models.PositiveIntegerField()  # Количество проданных товаров
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )  # Цена товара
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.product_name


def save(self, *args, **kwargs):
    if self.available_quantity < self.sold_quantity:
        raise Exception('Количество доступных товаров должно быть больше количества проданных товаров')
    super().save(*args, **kwargs)


