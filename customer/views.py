from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Customer
from .serializer import CustomerSerializer

class CustomerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 20

    
class CustomerView(viewsets.ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = CustomerPagination