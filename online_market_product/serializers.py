from rest_framework.serializers import ModelSerializer

from online_market_app.models import OnlineMarketUser
from .models import Product


class ProductUser(ModelSerializer):
    class Meta:
        model = OnlineMarketUser
        fields = (
            "id",
            "username",
        )


class ProductSerializer(ModelSerializer):
    user = ProductUser()

    class Meta:
        model = Product
        fields = "__all__"


class ProductEditSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "user",
        )
