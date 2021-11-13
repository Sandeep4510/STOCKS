from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from nsepy import get_history
from datetime import date
import json


@api_view(["GET"])
def Health(req):
    return JsonResponse("Server Running", safe=False)


@api_view(["POST"])
def GetData(req):
    try:
        data = json.loads(req.body)
        stock = data["stock"]
        for i in ([stock]):
            data = get_history(symbol=i, start=date(2021, 8, 17), end=date(2021, 9, 17))  # duration
        print(data.get("Last"))
        print("*****************************************************************************")
        return JsonResponse("Calculating", status=status.HTTP_200_OK, safe=False)
    except Exception as e:
        return e
