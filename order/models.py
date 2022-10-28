from django.db import models

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

