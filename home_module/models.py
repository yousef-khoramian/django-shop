from django.db import models

# Create your models here.


class SiteBanner(models.Model):
    image=models.ImageField(upload_to='images/banners',verbose_name='تصویر')
    is_active=models.BooleanField(verbose_name='فعال',default=False)

    class Meta:
        verbose_name='بنر سایت'
        verbose_name_plural='بنر های سایت'


class SiteSettings(models.Model):
    about_us=models.TextField(verbose_name='درباره ی ما')
    email=models.EmailField(verbose_name='ایمیل')
    phone_number=models.IntegerField(verbose_name='شماره ی تماس')
    telegram_user_name=models.CharField(null=True,blank=True,verbose_name='نام کاربری تلگرام')
    github_user_name=models.CharField(null=True,blank=True,verbose_name='نام کاربری گیت هاب')
    linkedin_user_name=models.CharField(null=True,blank=True,verbose_name='نام کاربری لینکدین')
    is_active=models.BooleanField(verbose_name='فعال')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='تنظیمات سایت'