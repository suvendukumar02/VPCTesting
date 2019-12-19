from django.urls import path

from .views import api_health_check_view

urlpatterns = [
    path('health/', api_health_check_view, name='api_health_check_view')
]