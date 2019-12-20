from django.db import models

class Order(models.Model):
    # ID = models.IntegerField(primary_key=True)
    OrderNumber = models.CharField(max_length=7, default="0"*7, primary_key=True)
    # test = models.CharField(max_length=20)
    class Meta:
        db_table = "Order"


class OrderDetails(models.Model):
    ID = models.IntegerField(primary_key=True)
    OrderNumber = models.ForeignKey(
        to="order.Order",
        to_field="OrderNumber",
        on_delete=models.CASCADE,
        db_column='OrderNumber',
        null=True)
    # OrderNumber = models.CharField(max_length=17, default="?"*17)
    Category = models.CharField(max_length=17, default="?"*17)
    Product = models.CharField(max_length=27, default="?"*27)
    ProductPrice = models.FloatField(default=0.0)
    DatePurchased = models.DateField(auto_now=False)

    class Meta:
        db_table = "OrderDetails"

