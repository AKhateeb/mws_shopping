from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderView

app_name = "order"

order_router = DefaultRouter()
order_router.register("orders", OrderView)

urlpatterns = order_router.urls
# urlpatterns = [
#     path('', include("order.urls", namespace="order")),
# ]
