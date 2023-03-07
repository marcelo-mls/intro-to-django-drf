from django.urls import path, include
from rest_framework import routers
from todo.views import UserViewSet, TaskViewSet


# 5 - Quinta Etapa (proximo passo em config/urls.py)
router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
