import requests
from django.http import HttpResponse


def health_check_view(request):
    response = requests.get("http://18.140.113.67:9000/api/health/")
    return HttpResponse('Hello, World! <br><br>From API Server: ' + str(response.json()['timestamp']))
