from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "order"

order_router = DefaultRouter()
order_router.register("orders", OrderView)
urlpatterns = order_router.urls

urlpatterns += [
    path("freq_together/", freq_together),
    path("get_recommends/", get_recommends),
    path("predict_sales/", predict_sales),
    path("find_corelate_product/", find_corelate_product),
]

# urlpatterns = [
#     path('', include("order.urls", namespace="order")),
# ]
