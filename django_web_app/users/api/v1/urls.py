from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import UserApiView  

router = DefaultRouter()
router.register(r"users", UserApiView, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
