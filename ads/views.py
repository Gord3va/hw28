import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ads


def index(request):
    responce = {'status': 'ok'}
    return JsonResponse(responce, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.pk,
                "name": category.name

            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        categories_data = json.loads(request.body)

        cat = Categories(**categories_data)

        cat.save()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        }, status=201, json_dumps_params={"ensure_ascii": False})


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        }, status=201, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()

        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published

            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = Ads(**ads_data)

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        }, status=201, json_dumps_params={"ensure_ascii": False})


class AdsDetailView(DetailView):
    model = Ads

    def get(self, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        }, status=201, json_dumps_params={"ensure_ascii": False})
