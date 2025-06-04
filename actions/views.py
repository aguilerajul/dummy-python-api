import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import DailyAction


@csrf_exempt
def register_action(request):
    """Register a daily action via POST request."""

    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        payload = json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    action = payload.get("action")
    valid_actions = {choice[0] for choice in DailyAction.ACTION_CHOICES}
    if action not in valid_actions:
        return JsonResponse({"error": "Invalid action"}, status=400)

    record = DailyAction.objects.create(action=action)
    return JsonResponse({"id": record.id, "description": record.description()})
