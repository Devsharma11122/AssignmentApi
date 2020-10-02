from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import *
from . models import Products



def home(request):
        a="<h1>To create or Read data go to link : 127.0.0.1:8000/product_list/</h1><br>"
        b="<h1>To Update or Delete data go to link : 127.0.0.1:8000/product_list/(id)</h1><br>"
        c=a+b
        return HttpResponse(c)


class ProductList(APIView):
    # function to get all the products from the database
    def get(self, request):
        model = Products.objects.all()
        serializer = ProductSerializer(model , many=True)
        return Response(serializer.data)

    #function create a new product in database
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    #function to fetch the details of product of a given product_id 
    def get_product(self, product_id):
        try:
            model = Products.objects.get(id = product_id)
            return model
        except Products.DoesNotExist:
            return Response('Product with id {} does not exists'.format(product_id))


    # function to serialize the result of function get_product()
    def get(self, request, product_id):
        serializer = ProductSerializer(self.get_product(product_id))
        return Response(serializer.data)


    # function to edit/update the data of particular id in the database
    def put(self, request, product_id):
        serializer = ProductSerializer(self.get_product(product_id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # function to delete the product on given product_id
    def delete(self, request, product_id):
        model = self.get_product(product_id)
        model.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



# authentication for user
class UserAuthentication(ObtainAuthToken):
    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user=user)
        return Response(token.key)