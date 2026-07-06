from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    count=models.IntegerField(verbose_name='تعداد')
    finally_price=models.IntegerField(verbose_name='قیمت نهایی')


    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبد های خرید'