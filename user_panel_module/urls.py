from . import views
from django.urls import path

urlpatterns=[
    path('',views.UserPanelView.as_view(),name='user_panel_page'),
    path('edit-profile/',views.EditUserProfile.as_view(),name='edit_profile_page'),
    path('edit-pass/',views.EditPasswordView.as_view(),name='edit_password_page'),
]