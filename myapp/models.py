from django.db import models
from datetime import date

# Create your models here.
class registered_people(models.Model):
    Name=models.CharField(max_length=20)
    Mobile=models.IntegerField()
    Email=models.EmailField(max_length=30)
    Course=models.CharField(max_length=20)
    Source=models.CharField(max_length=20)
    LeadStatus=models.CharField(max_length=20)
    DemoDate=models.DateField()
    Counsler=models.CharField(max_length=20)
    Remarks=models.CharField(max_length=20)

class joining_people(models.Model):
    Name=models.CharField(max_length=20)
    Course=models.CharField(max_length=20)
    DateOfJoining=models.DateField()
    DateOfCompletion=models.DateField()
    #CourseFee=models.IntegerField()
    Instructor=models.CharField(max_length=20)
    #AadharNo=models.IntegerField()
    Email=models.EmailField(max_length=30)
    Mobile=models.IntegerField()
    Remarks=models.CharField(max_length=20)
    


