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

@api_view(["POST"])
def GetData(req):
    try:
        print(req)
        a = ["INFY", "SBIN"]  # stock name
        for i in (a):
            data = get_history(symbol=i, start=date(2021, 8, 17), end=date(2021, 9, 17))  # duration
            print(data.get("Last"))
            print("*****************************************************************************")
            return JsonResponse("hello world",safe=False)
            # return JsonResponse( data.get("Last"),safe=False)
    except Exception as e:
        return e
# Create your views here.
