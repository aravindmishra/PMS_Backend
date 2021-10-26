from django.db import models

# Create your models here.
class MedicineDetails(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    rack_no = models.IntegerField(blank=True,null=True)
    medicine_name = models.CharField(max_length=500,blank=True,null=True,db_index=True, unique=True)
    brand = models.CharField(max_length=500,blank=True,null=True)
    power = models.CharField(max_length=200,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "medicine_details"