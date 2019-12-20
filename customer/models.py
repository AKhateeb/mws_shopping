from django.db import models

class Customer(models.Model):
    ID = models.IntegerField(primary_key=True)
    MaritalStatus = models.CharField(max_length=7, default="?"*7)
    Gender = models.CharField(max_length=7, default="?"*7)
    Income = models.IntegerField(default=0)
    Children = models.IntegerField(default=0)
    Education = models.CharField(max_length=19, default="?"*19)
    Occupation = models.CharField(max_length=19, default="?"*19)
    HomeOwner = models.CharField(max_length=3, default="?"*3)
    Cars = models.IntegerField(default=0)
    CommuteDistance = models.CharField(max_length=10, default="?"*10)        
    Region = models.CharField(max_length=13, default="?"*13)      
    Age = models.IntegerField(default=0)      
    Buy = models.CharField(max_length=3, default="?"*3)  
    # OrderNumber = models.CharField(max_length=30, default="?"*3)  
    # OrderNo = models.ForeignKey(
    #     to="order.Order",
    #     to_field="OrderNumber",
    #     on_delete=models.CASCADE,
    #     db_column='OrderNumber')


    class Meta:
        db_table = "Customer"