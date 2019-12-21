from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "customer"

customer_router = DefaultRouter()
customer_router.register("customers", CustomerView)

urlpatterns = customer_router.urls

urlpatterns += [
    path("cust_will_buy/", CustomerWillBy),
    path("cust_category/", CustomerClassified),
]
# urlpatterns = [
#     path('', include("customer.urls", namespace="customer")),
# ]
