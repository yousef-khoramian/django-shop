from . import views
from django.urls import path

urlpatterns=[
    path('',views.UserBasketView.as_view(),name='user_basket_page'),
    path('add-to-order',views.add_to_order,name='add_to_order_page'),
    path('delete-order',views.delete_order,name='delete_order_page'),
    path('change-count',views.change_count,name='change_count_page'),
]