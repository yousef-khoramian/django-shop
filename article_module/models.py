from django.db import models
from jalali_date import datetime2jalali
from account_module.models import User


# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    author_description = models.TextField(verbose_name='توضیحات نویسنده')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', null=True)
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    short_description = models.CharField(max_length=300, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات', null=True)
    create_date_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ و ساعت ساخت')
    is_active = models.BooleanField(verbose_name='فعال', default=False)

    def __str__(self):
        return f'{self.title} / {self.user.email}'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def detail_url(self):
        return f'/article/{self.slug}/'

    def date(self):
        return datetime2jalali(self.create_date_time).strftime('%Y/%m/%d')

    date.short_description = 'تاریخ'

    def time(self):
        return datetime2jalali(self.create_date_time).strftime('%H:%M')


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    parent = models.ForeignKey("ArticleComment", on_delete=models.CASCADE, verbose_name='جواب',blank=True,null=True)
    message = models.TextField(verbose_name='پیام')
    create_date_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و ساعت ساخت')

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = 'کامنت مقاله'
        verbose_name_plural = 'نظرات مقاله'

    def date(self):
        return datetime2jalali(self.create_date_time).strftime('%Y/%m/%d')
    date.short_description = 'تاریخ'

    def time(self):
        return datetime2jalali(self.create_date_time).strftime('%H:%M')
