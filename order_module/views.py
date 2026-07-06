from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from order_module.models import Order


# Create your views here.

@method_decorator(login_required,'dispatch')
class UserBasketView(TemplateView):
    template_name = 'order_module/user_basket_page.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        orders=Order.objects.filter(user_id=self.request.user.id)
        price=0
        for order in orders:
            price+=order.finally_price
        context['orders']=Order.objects.filter(user_id=self.request.user.id)
        context['order_price']=price
        return context


def add_to_order(request:HttpRequest):
    product_id=request.GET.get('product_id')
    count=int(request.GET.get('count'))
    order=Order.objects.filter(product_id=product_id).first()
    if order:
        order.count+=count
        finally_price = order.product.price * order.count
        order.finally_price = finally_price
        order.save()
    else:
        new_order = Order(user_id=request.user.id, product_id=product_id, count=count)
        finally_price = new_order.product.price * count
        new_order.finally_price = finally_price
        new_order.save()


def delete_order(request:HttpRequest):
    product_id=request.GET.get('product_id')
    order=Order.objects.filter(user_id=request.user.id,product_id=product_id)
    order.delete()
    orders = Order.objects.filter(user_id=request.user.id)
    price = 0
    for order in orders:
        price += order.finally_price
    context={
        'orders':Order.objects.filter(user_id=request.user.id),
        'order_price':price
    }
    return render(request,'order_module/user_basket_componenet.html',context)


def change_count(request:HttpRequest):
    product_id = request.GET.get('product_id')
    status = request.GET.get('status')
    order=Order.objects.filter(user_id=request.user.id,product_id=product_id).first()
    if status=='increase':
        order.count+=1
        finally_price = order.product.price * order.count
        order.finally_price = finally_price
        order.save()
    if status=='decrease':
        order.count-=1
        finally_price = order.product.price * order.count
        order.finally_price = finally_price
        order.save()
        if order.count==0:
            order.delete()
    orders = Order.objects.filter(user_id=request.user.id)
    price = 0
    for order in orders:
        price += order.finally_price
    context = {
        'orders': Order.objects.filter(user_id=request.user.id),
        'order_price': price
    }
    return render(request, 'order_module/user_basket_componenet.html', context)