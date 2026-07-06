from PIL.PngImagePlugin import is_cid
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from utils.convertors import group_list
from product_module.models import Product, Brand, ProductImages


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list_page.html'
    model = Product
    ordering = '-id'
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        search = self.request.GET.get('search')
        start_price=self.request.GET.get('start_price')
        end_price=self.request.GET.get('end_price')
        if start_price:
            query=query.filter(price__gte=start_price)
        if end_price:
            query = query.filter(price__lte=end_price)
        if search is not None:
            query = query.filter(title__icontains=search)
        if self.kwargs:
            brands = self.kwargs.get('brand')
            query = query.filter(brand__url_title=brands)
        return query

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_obj=context.get('page_obj')
        paginator=context.get('paginator')
        current=page_obj.number
        total=paginator.num_pages
        start=max(1,current-4)
        end=min(total,current+5)
        if total>10:
            if current < 6:
                custom_range = range(1, 11)
            else:
                custom_range = range(start, end + 1)
        else:
            custom_range=range(1,total+1)
        context['custom_range']=custom_range
        context['brands'] = Brand.objects.filter(is_active=True)
        context['start_price'] = self.request.GET.get('start_price') or Product.objects.all().order_by('price').first().price
        context['end_price'] = self.request.GET.get('end_price') or Product.objects.all().order_by('-price').first().price
        context['min_price'] = Product.objects.all().order_by('price').first().price
        context['max_price'] = Product.objects.all().order_by('-price').first().price
        return context


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail_page.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brands'] = Brand.objects.filter(is_active=True)
        related_product = Product.objects.filter(brand=self.object.brand).exclude(id=self.object.id)
        context['related_product'] = group_list(related_product, 3)
        images = ProductImages.objects.filter(product_id=self.object.id, is_active=True)
        context['product_images']=group_list(images,3)
        return context
