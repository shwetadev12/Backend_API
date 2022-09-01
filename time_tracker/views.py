from urllib import request
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerialzer
# Create your views here.

class CreateUserAPIView(CreateAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerialzer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ValidationError("username and password required.")
        
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return Response("User created successfully.")


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerialzer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user =  User.objects.filter(id = self.kwargs['pk'])
        return user