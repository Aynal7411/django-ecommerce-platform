
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from  product.models import ProductItem


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def subtotal(self):
      return sum(
        item.product_item.final_price * item.quantity
        for item in self.items.all()
       )

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name="items")
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    @property
    def subtotal(self):
      return self.product_item.final_price * self.quantity
