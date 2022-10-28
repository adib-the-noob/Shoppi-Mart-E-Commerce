from django.db import models
from django.core.validators import MinValueValidator
from uuid import uuid4


# Create your models here.
from django.db import models
from store.models import Product
from user.models import Address
# Create your models here.

# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]