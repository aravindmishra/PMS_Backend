from django.db import models

# Create your models here.
class PurchaseDetails(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True,null=True)
    medicine_id = models.IntegerField(blank=True,null=True)
    purchased_qty = models.IntegerField(blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "purchase_details"


class CustomerDetails(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=False,null=False)
    mobile_no = models.BigIntegerField(blank=False,null=False)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "customer_details"