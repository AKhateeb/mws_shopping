from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Customer
from order.models import OrderDetails, Order
from .serializer import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Sum


def return_response(data, is_valid=False):
    # status_code = 200
    return JsonResponse(data, safe=False)
    # status_code = status.HTTP_200_OK if is_valid else status.HTTP_400_BAD_REQUEST

class CustomerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 20

    
class CustomerView(viewsets.ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = CustomerPagination


def CustomerClassified(request):
    # cust_id = request.data.get('cust_id', None)
    # cust_orders = Customer.objects.filter(pk=cust_id).values('OrderNumber__Product')
    # qry = OrderDetails.objects.filter(Product__in=ids).values('Product')
    Products = OrderDetails.objects.all().values('Category').distinct()[:100:5]

    data = list(Products)
    return return_response(data, True)

def CustomerWillBy(request):
    # cust_id = request.data.get('cust_id', None)
    # cust_orders = Customer.objects.filter(pk=cust_id).values('OrderNumber__Product')
    # qry = OrderDetails.objects.filter(Product__in=ids).values('Product')
    
    Products = OrderDetails.objects.all().values('Product')[:450:50]
    data = {'possibility_to_buy': 74.554}
    return return_response(data, True)

