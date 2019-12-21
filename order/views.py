from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import Order, OrderDetails
from customer.models import Customer
from .serializer import OrderSerializer
from django.http.response import JsonResponse
from django.db.models import Sum


KEYS = {
    'commute_list': [
        "0-1 Miles",
        "1-2 Miles",
        "2-5 Miles",
        "5-10 Miles",
        "10+ Miles",
    ]
}

def get_customer_attributes(data):
    return Customer.objects.all()

def return_response(data, is_valid=False):
    # status_code = 200
    return JsonResponse(data, safe=False)

class OrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 20


class OrderView(ModelViewSet):
    model = OrderDetails
    serializer_class = OrderSerializer
    queryset = OrderDetails.objects.all()
    pagination_class = OrderPagination


def get_recommends(request):
    Products = OrderDetails.objects.all().values('Product').distinct()[5:100:5]
    data = list(Products)
    return return_response(data, True)

def freq_together(request):
    # products = request.data.get('products', "")
    # prods = products.split(",")
    # orders = (
    #     OrderDetails.objects
    #     .filter(Product__in=prods)
    #     .values('OrderNumber')
    # )
    Products = OrderDetails.objects.all().values('Product').distinct()[:15:5]
    data = list(Products)
    return return_response(data, True)

def predict_sales(request):
    # ids = request.data.get('products', None)
    qry = OrderDetails.objects.filter(ProductPrice__gt=50).aggregate(predicted_sales=Sum('ProductPrice'))
    data = qry
    return return_response(data, True)

def find_corelate_product(request):
    # ids = request.data.get('products', None)
    # qry = OrderDetails.objects.filter(Product__in=ids).values('Product')
    Products = OrderDetails.objects.all().values('Product')[:105:50]
    
    data = list(Products)

    return return_response(data, True)



