from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Product
from .serializers import ProductSerializer, ProductEditSerializer
from online_market_app.online_market_decorators import required_fields


class ProductsView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductSerializer
        else:
            return ProductEditSerializer

    @required_fields()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            data = {
                "status": HTTP_201_CREATED,
                "success": True,
                "message": "Product created successfully",
            }
            return Response(data, status=HTTP_201_CREATED)
        else:
            data = {
                "status": HTTP_400_BAD_REQUEST,
                "success": False,
                "errors": serializer.errors,
                "message": "Product creation failed",
            }
            return Response(data, status=HTTP_400_BAD_REQUEST)


class ProductDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
