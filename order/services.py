from django.db import transaction

from cart.models import Cart
from .models import Order, OrderItem


@transaction.atomic
def create_order_from_cart(cart):

    # Step 1: Check if cart is empty
    if not cart.items.exists():
        raise ValueError("Cannot create order from an empty cart.")

    # Step 2: Get cart items
    cart_items = cart.items.select_related(
        "product_item",
        "product_item__product",
    )

    # Step 3: Validate stock
    for cart_item in cart_items:

        product_item = cart_item.product_item

        if product_item.stock < cart_item.quantity:
            raise ValueError(
                f"Insufficient stock for {product_item}"
            )

    # Step 4: Create Order
    order = Order.objects.create(
        user=cart.user,
        subtotal=0,
        discount=0,
        shipping_cost=0,
        total=0,
    )

    subtotal = 0

    # Step 5: Create OrderItems
    for cart_item in cart_items:

        product_item = cart_item.product_item

        price = product_item.final_price

        item_subtotal = price * cart_item.quantity

        OrderItem.objects.create(
            order=order,
            product_item=product_item,
            product_name=product_item.product.name,
            sku=product_item.sku or "",
            size=product_item.size,
            color=product_item.color,
            price=price,
            quantity=cart_item.quantity,
            subtotal=item_subtotal,
        )

        subtotal += item_subtotal

    # Step 6: Calculate Order total

    shipping_cost = 0
    discount = 0

    total = subtotal + shipping_cost - discount

    order.subtotal = subtotal
    order.shipping_cost = shipping_cost
    order.discount = discount
    order.total = total

    order.save(
        update_fields=[
            "subtotal",
            "shipping_cost",
            "discount",
            "total",
        ]
    )

    # Step 7: Reduce stock
    for cart_item in cart_items:

        product_item = cart_item.product_item

        product_item.stock -= cart_item.quantity
        product_item.save(update_fields=["stock"])

    # Step 8: Clear cart
    cart.items.all().delete()

    return order