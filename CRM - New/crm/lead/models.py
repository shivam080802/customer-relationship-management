from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class leadModel(models.Model):
    source_choice = (("call","call"),
                     ("employee", "Employee Ref"),
                     ("external","External Ref"))
    created_at = models.DateTimeField(auto_now_add=True)
    leadOwner = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    customerName = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=100)
    email=models.EmailField()
    address = models.CharField(max_length=100)
    leadTitle = models.CharField(max_length = 100)
    leadSource = models.CharField(max_length=100)
    expectedDate = models.CharField(blank=True, null=True,max_length=100)
    needType = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100, default="New")
    remarks = models.CharField(max_length=100,blank=True)



class companyModel(models.Model):
    companyName = models.CharField(max_length=100, unique=True)
    customerName = models.CharField(max_length=100)
    mobileNumber = models.CharField(max_length=100)
    email=models.EmailField()
    address = models.CharField(max_length=100)

class userModel(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
