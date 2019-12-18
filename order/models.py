from django.db import models

class Order(models.Model):
    OrderNumber = models.CharField(max_length=7, default="0"*7)
    
    class Meta:
        db_table = "Order"


class OrderDetails(models.Model):
    # ID = models.IntegerField(primary_key=True)
    OrderNumber = models.ForeignKey(to="order.Order", on_delete=models.CASCADE)
    Category = models.CharField(max_length=17, default="؟"*17)
    Product = models.CharField(max_length=27, default="؟"*27)
    ProductPrice = models.FloatField(default=0.0)
    DatePurchased = models.DateField(auto_now=False)

    class Meta:
        db_table = "OrderDetails"

