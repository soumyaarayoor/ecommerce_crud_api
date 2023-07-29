from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Customer, Product
from .serializer import CustomerSerializer, ProductSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Customer, Product
from .serializer import CustomerSerializer, ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Check if the product is registered before 2 months
        if 'is_active' in request.data and not instance.is_registered_before_2_months():
            return Response({'error': 'Product cannot be deactivated yet.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

