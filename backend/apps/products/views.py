from django.shortcuts import render
from rest_framework import generics 
from .serializers import ProductSerializer

# Create your views here.
from .models import Product

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


