from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import OnlineMarketUser, Role
from .serializers import RegistrationUserSerializer, RoleSerializer
from .online_market_decorators import required_fields


class RegistrationUserView(CreateAPIView):

    queryset = OnlineMarketUser.objects.all()
    serializer_class = RegistrationUserSerializer

    @required_fields()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            data = {
                "status": HTTP_201_CREATED,
                "success": True,
                "message": "Registration successfull",
            }
            return Response(data, status=HTTP_201_CREATED)
        else:
            data = {
                "status": HTTP_400_BAD_REQUEST,
                "success": False,
                "errors": serializer.errors,
                "message": "Registration failed",
            }
            return Response(data, status=HTTP_400_BAD_REQUEST)


class RolesView(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
