from django.urls import path
from .views import CreateUserAPIView, UserRetrieveUpdateDestroyAPIView


urlpatterns = [
      path('user/create/', CreateUserAPIView.as_view()),
      path('user/retrieve_update_destroy/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),

]