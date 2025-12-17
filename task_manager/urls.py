from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from task.views import TaskViewSet, random_joke, task_report

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/joke/', random_joke),
    path('api/report/', task_report),
]
