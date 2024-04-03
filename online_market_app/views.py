from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegistrationUserSerializer


class RegistrationUserView(APIView):
    
    def post(self, request):
        data = {}
        serializer = RegistrationUserSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.save()
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username

        else:
            data = serializer.errors

        return Response(data)