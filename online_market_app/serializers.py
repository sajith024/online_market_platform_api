from rest_framework.serializers import ModelSerializer, ValidationError, CharField

from .models import OnlineMarketUser, Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RegistrationUserSerializer(ModelSerializer):
    password1 = CharField()
    password2 = CharField()

    class Meta:
        model = OnlineMarketUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "role",
        )

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        user = OnlineMarketUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            role=validated_data["role"],
        )

        user.set_password(validated_data["password1"])
        user.save()

        return user
