from django.db import models
from jalali_date import date2jalali
from account_module.models import User


# Create your models here.


class ContactUs(models.Model):
    user_name=models.CharField(max_length=300,verbose_name='نام کاربری')
    email=models.EmailField(verbose_name='ایمیل')
    message=models.TextField(verbose_name='پیام')
    create_date=models.DateField(auto_now_add=True,verbose_name='تاریخ ارسال')

    def __str__(self):
        return f'{self.user_name} / {self.email}'

    class Meta:
        verbose_name='تماس'
        verbose_name_plural='تماس ها'

    def date(self):
        return date2jalali(self.create_date).strftime('%Y/%m/%d')
    date.short_description='تاریخ ساخت'