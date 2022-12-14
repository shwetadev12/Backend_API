from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Project, TimeLog
from .serializers import ProjectSerializer, TimelogSerializer, UserSerializer

# Create your views here.


class CreateUserAPIView(CreateAPIView):
    """View for create the user"""

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "status": status.HTTP_201_CREATED,
            "message": "User Created Successfully",
            "data": serializer.data,
        }
        return response


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """View for retrieve, update, delete user"""

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = User.objects.filter(id=self.kwargs["pk"])
        return user


class ProjectAPIView(APIView):
    """Apiview for the CRUD operation of the project"""

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise ValidationError("No project found with the given id")

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            data = self.get_object(pk)
            serializer = ProjectSerializer(data)
        else:
            data = Project.objects.all()
            serializer = ProjectSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "status": status.HTTP_201_CREATED,
            "message": "Project Created Successfully",
            "data": serializer.data,
        }
        return response

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        project_to_update = self.get_object(pk)
        serializer = ProjectSerializer(
            instance=project_to_update, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "status": status.HTTP_200_OK,
            "message": "Project Updated Successfully",
            "data": serializer.data,
        }
        return response

    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk")
        project_to_delete = self.get_object(pk)
        resp = project_to_delete.delete()
        response = Response()
        response.data = {
            "status": status.HTTP_204_NO_CONTENT,
            "message": "Project Deleted Successfully"
            }
        return response

class TimelogAPIView(APIView):
    """Apiview for the CRUD operation of the Timelog"""

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return TimeLog.objects.get(pk=pk)
        except TimeLog.DoesNotExist:
            raise ValidationError("No Timelog available for given ID")

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            data = self.get_object(pk)
            serializer = TimelogSerializer(data)
        else:
            data = TimeLog.objects.all()
            serializer = TimelogSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TimelogSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "status": status.HTTP_201_CREATED,
            "message": "Timelog Created Successfully",
            "data": serializer.data,
        }
        return response

    def put(self, request, pk=None):
        timelog_to_update = self.get_object(pk)
        serializer = TimelogSerializer(
            instance=timelog_to_update, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "status": status.HTTP_200_OK,
            "message": "Timelog Updated Successfully",
            "data": serializer.data,
        }
        return response

    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk")
        timelog_to_delete = self.get_object(pk)
        timelog_to_delete.delete()
        return Response({
            "status":status.HTTP_204_NO_CONTENT,
            "message": "Timelog Deleted Successfully"
            })
