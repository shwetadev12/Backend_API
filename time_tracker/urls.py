from django.urls import path
from .views import (
    CreateUserAPIView,
    UserRetrieveUpdateDestroyAPIView,
    ProjectAPIView,
    TimelogAPIView,
)


urlpatterns = [
    path('user/register/', CreateUserAPIView.as_view()),
    path('user/retrieve_update_destroy/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('project/', ProjectAPIView.as_view()),
    path('project/<int:pk>/', ProjectAPIView.as_view()),
    path('timelog/', TimelogAPIView.as_view()),
    path('timelog/<int:pk>/', TimelogAPIView.as_view()),
]