from rest_framework.routers import DefaultRouter
from ..viewsets.task_viewsets import taskViewsets

router = DefaultRouter()

router.register('book', taskViewsets, basename="taskViewsets")