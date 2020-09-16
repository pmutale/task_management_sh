from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from app import views

# router = routers.DefaultRouter()
# router.register(r'task/get_all', views.TaskViewSet)
# router.register(r'task/completed', views.TaskCompletedViewSet)
# router.register(r'task/delete', views.TaskDeleteViewSet)
# router.register(r'task/edit', views.TaskEditViewSet)

urlpatterns = [
    path('task/', views.TaskList.as_view()),
    path('task/<int:pk>/', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)