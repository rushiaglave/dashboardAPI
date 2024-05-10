from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Agedistribution, Monthlydistribution ,Policestdistribution, Yearlydistribution, unidentifieddeadbodies
from .serializers import AgeSerializer, MonthlySerializer, PoliceStationSerializer, YearwiseSerializer, UnidentifiedBodies
# Create your views here.
@api_view(['GET'])
def agelist(request):
        age = Agedistribution.objects.all()
        serializer =AgeSerializer(age, many=True)
        return Response(serializer.data, content_type='application/json')

@api_view(['GET'])
def monthlylist(request):
        monthly = Monthlydistribution.objects.all()
        serializer =MonthlySerializer(monthly, many=True)
        return Response(serializer.data, content_type='application/json')

@api_view(['GET'])
def PoliceStlist(request):
        PoliceStations = Policestdistribution.objects.all()
        serializer =PoliceStationSerializer(PoliceStations, many=True)
        return Response(serializer.data, content_type='application/json')


@api_view(['GET'])
def yearlylist(request):
        yearly = Yearlydistribution.objects.all()
        serializer =YearwiseSerializer(yearly, many=True)
        return Response(serializer.data, content_type='application/json')
   
@api_view(['GET'])
def unidentifiedBodiesList(request):
        deadBodies = unidentifieddeadbodies.objects.all()
        serializer = UnidentifiedBodies(deadBodies,many=True)
        return Response(serializer.data, content_type='application/json')

# @api_view(['POST'])
# def taskcreate(request):
#         Serializer =employeesSerializer(data=request.data)

#         if Serializer.is_valid():
#                 Serializer.save()

#         return Response(Serializer.data)

# @api_view(['POST'])
# def taskupdate(request, pk):
#         employees1 = employees.objects.get(id=pk)
#         Serializer =employeesSerializer(instance=employees1, data=request.data)

#         if Serializer.is_valid():
#                 Serializer.save()
                
#         return Response(Serializer.data)

# @api_view(['DELETE'])
# def taskdelete(request, pk):
#         employees1 = employees.objects.get(id=pk)
#         employees1.delete()

                
#         return Response('item deleted successefuly')