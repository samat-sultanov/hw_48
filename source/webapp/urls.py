from django.urls import path
from webapp.views import index_view, product_view, delete_product, create_product, update_product

urlpatterns = [
    path('', index_view, name="index_view"),
    path('product/<int:pk>/', product_view, name="product_view"),
    path('product/<int:pk>/delete/', delete_product, name="delete_product"),
    path('product/add/', create_product, name="create_product"),
    path('product/<int:pk>/update/', update_product, name="update_product"),
]
