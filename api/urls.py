from django.urls import path
from .views import MyAPIView

urlpatterns = [
    path('api/my-api/', MyAPIView.as_view()),
]
