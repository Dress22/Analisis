from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('comprar/<int:pk>/', views.purchase_product, name='purchase_product'),
]