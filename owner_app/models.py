from django.db import models

# Create your models here.


class OwnerRent(models.Model):
    division=models.CharField(max_length=20,null=True,blank=True)
    district=models.CharField(max_length=20,null=True,blank=True)
    property_location=models.TextField(max_length=100,null=True,blank=True)
    rent_money=models.IntegerField(null=True,blank=True,max_length=20)
    rent_currency=models.CharField(max_length=10,null=True,blank=True)
    floor_no=models.CharField(null=True,blank=True,max_length=20)
    floor_face=models.CharField(null=True,blank=True,max_length=50)
    plot_area=models.TextField(max_length=100,null=True,blank=True)
    are_types=models.CharField(max_length=10,null=True,blank=True)
    area_description=models.TextField(max_length=250,null=True,blank=True)
    rent_photo=models.ImageField(upload_to='rent',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True,blank=True,null=True)


    # def __str__(self):
    #     return self.
