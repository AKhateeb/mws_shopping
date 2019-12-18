from django.db import models

class Customer(models.Model):
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
    OrderNumber = models.ForeignKey(to="order.Order", on_delete=models.CASCADE)


    class Meta:
        db_table = "Customer"