from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def api_health_check_view(request):
    return JsonResponse({
        "timestamp": str(datetime.utcnow())
    })
