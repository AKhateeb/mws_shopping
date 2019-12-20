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
    status_code = status.HTTP_200_OK if is_valid else status.HTTP_400_BAD_REQUEST
    return Response(data, status=status_code)

class OrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 20


class OrderView(ModelViewSet):
    model = OrderDetails
    serializer_class = OrderSerializer
    queryset = OrderDetails.objects.all()
    pagination_class = OrderPagination


class FindOrderView(APIView):
    
    @action(methods=['GET'], detail=False, name='get orders of a customer attributes')
    def by_customer(self, request):
        customer_queryset = get_customer_attributes(data=request.data)
        data = list(customer_queryset)
        return return_response(data, True)
