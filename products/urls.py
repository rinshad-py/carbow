from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),

    path('products_list/', views.list_products, name='list_product'),
    path('products_details/<pk>', views.detail_product, name='detail_product'),
    

]