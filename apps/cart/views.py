from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.shops.models import Product
from .models import Cart, CartItem, Order, OrderItem


def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})


def add_to_cart(request, product_id):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    product = Product.objects.get(id=product_id)

    # Проверяем, есть ли уже такой товар в корзине
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

    return redirect('view_cart')


def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')


def place_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    order = Order.objects.create(user=request.user)

    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity
        )

    # Clear the cart
    cart_items.delete()
    order.save()

    return redirect('view_cart')


@login_required
def save_order_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')

        # Сохранение данных в админке или в профиле пользователя

        return redirect('order_confirmation')

    return redirect('view_cart')


@login_required
def order_confirmation(request):
    # Дополнительное представление для подтверждения заказа
    return render(request, 'cart/order_confirmation.html')

# Create your views here.

