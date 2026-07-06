from django.shortcuts import render
from django.views.generic import TemplateView

from product_module.models import Product, Brand
from utils.convertors import group_list
from home_module.models import SiteBanner


# Create your views here.



class HomePageView(TemplateView):
    template_name = 'home_module/home_page.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['banners']=SiteBanner.objects.filter(is_active=True)
        context['products']=Product.objects.filter(is_active=True)
        product_list=Product.objects.all().order_by('-id')[:12]
        context['group_list']=group_list(product_list,4)
        context['brands']=Brand.objects.filter(is_active=True)
        return context