from django.db import models

# Create your models here.


class Brand(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    url_title=models.CharField(max_length=300,verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name='برند'
        verbose_name_plural='برند ها'

class ProductImages(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE,verbose_name='محصول')
    image=models.ImageField(upload_to='images/product_images',verbose_name='تصویر')
    is_active=models.BooleanField(verbose_name='فعال')

    class Meta:
        verbose_name='تصویر محصول'
        verbose_name_plural='تصاویر محصول'

class Product(models.Model):
    category_choices=[
        ('popular_products','محصولات محبوب'),
        ('trending_products','محصولات مد')
    ]
    title=models.CharField(max_length=100,verbose_name='عنوان')
    slug=models.SlugField(verbose_name='اسلاگ',null=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name='برند',null=True)
    category=models.CharField(max_length=300,choices=category_choices,null=True,blank=True,verbose_name='دسته بندی')
    price=models.IntegerField(verbose_name='قیمت')
    image=models.ImageField(upload_to='images/products',verbose_name='تصویر')
    is_active=models.BooleanField(verbose_name='فعال')


    def __str__(self):
        return f'{self.title} / {self.price}'


    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'


    def detail_url(self):
        return f'/product/{self.slug}/'


