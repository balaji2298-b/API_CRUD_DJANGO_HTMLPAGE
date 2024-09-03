from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Employee
from myapp.serializers import Page
from rest_framework import status
from rest_framework import serializers

@api_view(['GET'])
def ApiOverview(request):
	myapp_urls ={
	            'all_pages':'/',
	            'Add': '/insert',
	            'Display': '/display',
	            'Update': '/update',
	            'Delete': '/delete'
	}
	return Response (myapp_urls)
@api_view(['POST'])
def add_items(request):
	page = Page(data=request.data)

	if Employee.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if page.is_valid():
		page.save()
		return Response(page.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def view_items(request):
	if request.query_params:
		pages = Employee.objects.filter(**request.query_params.dict())
	else:
		pages = Employee.objects.all()

	if pages:
		serializer = Page(pages, many=True)
		return Response(serializer.data)

	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_items(request,mobilenumber):
     page = Employee.objects.get(mobilenumber=mobilenumber)
     data = Page(instance=page, data=request.data)

     if data.is_valid():
     	data.save()
     	return Response(data.data)

     else:
     	return_Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request,pk):
	page = Employee.objects.get(pk=pk)
	page.delete()
	return Response(status=status.HTTP_404_NOT_FOUND)




	
	
	