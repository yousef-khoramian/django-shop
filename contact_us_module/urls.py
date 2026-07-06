from . import views
from django.urls import path

urlpatterns=[
    path('',views.ContactUsView.as_view(),name='contact_us_page'),
]