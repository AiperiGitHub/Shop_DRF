from rest_framework import serializers
from  .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('__all__')
        extra_kwargs = {
            'product': {'read_only': True},
            'cart': {'read_only': True}
        }
        read_only_fields = ('product', 'cart')
        # write_only_fields = ()
        # depth = 1
        # max_depth = 1

