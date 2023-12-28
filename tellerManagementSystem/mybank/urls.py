from django.urls import path
from . import views

urlpatterns = [
    path('mybank/login', views.login_view),
    path('mybank/accountopening', views.account_opening_view),
    path('mybank/accountopening/existing_customer/<int:existing_account_num>',
         views.existing_customer_view),
    path('mybank/', views.home_page_view)
]
