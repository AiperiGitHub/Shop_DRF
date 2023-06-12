from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.shops.models import Product
from .models import Cart, CartItem, Order, OrderItem

# from django.views.decorators.csrf import csrf_exempt


class CartView(APIView):
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     cart = Cart.objects.get(user=request.user)
    #     cart_items = CartItem.objects.filter(cart=cart)
    #     serializer = CartItemSerializer(cart_items, many=True)
    #     return Response(serializer.data)

# def view_cart(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)
#     return render(request, 'cart/view_cart.html', {'cart_items': cart_items})


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)

        product = Product.objects.get(id=product_id)

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)

        return redirect('view_cart')


class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id):
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        return redirect('view_cart')


class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        order = Order.objects.create(user=request.user)

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity
            )

        cart_items.delete()
        order.save()

        return redirect('view_cart')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @csrf_exempt
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


