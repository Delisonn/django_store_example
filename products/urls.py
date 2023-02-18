
from django.urls import path

from products.views import products, basketAdd, basketRemove

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('baskets/add/<int:product_id>/', basketAdd, name='basketAdd'),
    path('baskets/remove/<int:basket_id>/', basketRemove, name='basketRemove'),
]
