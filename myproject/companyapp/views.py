from django.shortcuts import render
from .models import Companydb
from .serializers import Companydbserializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def companies(request):
    if request.method =='GET':
        companies=Companydb.objects.all()
        serializer=Companydbserializer(companies,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method =='POST':
        serializer=Companydbserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def company_id(request,id):
    try:
        Company=Companydbserializer.objects.get(pk=id)
    except Company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=Companydbserializer(Company)
        return JsonResponse(serializers.Data)
    if request.method=='PUT':
        serializers=Companydbserializer(Company,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        if request.method=='DELETE':
            Company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

