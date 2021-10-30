from django.db import models

# Create your models here.

class ConsultantForm(models.Model):
    name = models.CharField( max_length=30)  # Field name made lowercase.m
    email = models.EmailField(max_length=254) # field name for email in lowercase
    phone_no =  models.IntegerField()  # Field name made lowercase.m
    bank_ifsc = models.CharField(max_length=20)# field name for email in lowercase
    bank_acc_no = models.IntegerField() # Field name made lowercase.models
    exp = models.CharField( max_length=400,default='') 
    def __str__(self):
        return self.name