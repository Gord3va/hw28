from django.http import JsonResponse


def index(request):
    responce = {'status': 'ok'}
    return JsonResponse(responce, status=200)