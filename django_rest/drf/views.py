from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


def index(request):
    return HttpResponse('<h1>Hello Rest Api</h1>')


class WonderAPIView(APIView):
    # if methods GET this function called. Returns all records from db
    def get(self, request):
        wonders = Wonder.objects.all()
        return Response({'record': WonderSerializerCustom(wonders, many=True).data})

    # Includes key-value dict. Adds new record in db
    """{
            "title": "Мавзолей Тадж-Махал",
            "creator": "Шах Джахан I",
            "created": "1653-01-01",
            "place": "Агра",
            "current_status": "Exists"
        }
    """

    def post(self, request):
        serializer = WonderSerializerCustom(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({'Wonder created': serializer.data})

    # updates existing record. Requires primary key of record
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Ошибка': 'Не указал индентификатор объекта'})
        instance = Wonder.objects.get(pk=pk)
        serializer = WonderSerializerCustom(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Wonder': serializer.data})

    # deletes record by its primary key
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Ошибка': 'Не указал индентификатор объекта'})
        instance = Wonder.objects.get(pk=pk)
        deliting_wonder = instance.title
        instance.delete()
        return Response({'Deleted wonder': deliting_wonder})


# api/wonders/field/?q=башня serching in db. Not case-sensitive in english
class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        field_slug = kwargs.get('field_slug', None)
        query = request.query_params.get('q')
        filter_kwargs = {f"{field_slug}__icontains": query}
        wonders_query = Wonder.objects.filter(**filter_kwargs)
        serializer = WonderSerializerCustom(wonders_query, many=True)
        return Response({'Search result': serializer.data, 'Search field': field_slug})
