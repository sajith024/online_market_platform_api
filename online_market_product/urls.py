from django.urls import path

from .views import ProductDetailsView, ProductsView

urlpatterns = [
    path("api/products/", ProductsView.as_view(), name="products"),
    path("api/product/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
]
