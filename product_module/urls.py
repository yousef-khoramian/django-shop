from . import views
from django.urls import path

urlpatterns=[
    path('',views.ProductListView.as_view(),name='product_list_page'),
    path('brand/<brand>/',views.ProductListView.as_view(),name='product_brand_page'),
    path('<slug>/',views.ProductDetailView.as_view(),name='product_detail_page'),
]