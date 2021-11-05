from django.db import models

# Create your models here.
class PurchaseDetails(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True,null=True)
    medicine_id = models.IntegerField(blank=True,null=True)
    purchased_qty = models.IntegerField(blank=True,null=True,default=0)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "purchase_details"

    def purchase_list(filter = 0):
        query = "SELECT pd.purchase_id, cd.name as customer_name, cd.mobile_no, md.medicine_name, pd.purchased_qty, pd.created_date FROM purchase_details as pd INNER JOIN customer_details as cd ON cd.customer_id = pd.customer_id INNER JOIN medicine_details as md ON md.medicine_id = pd.medicine_id"
        if filter:
            print(filter)
            if filter["mobile_no"] and filter["medicine_name"]:
                print("ENTER 1")
                query = query + " WHERE cd.mobile_no={} AND LOWER(md.medicine_name) = LOWER('{}')".format(filter["mobile_no"],filter["medicine_name"])
                print(query)
            elif filter["mobile_no"]:
                print("ENTER 2")
                query = query + " WHERE cd.mobile_no={}".format(filter["mobile_no"])
            elif filter["medicine_name"]:
                print("ENTER 3")
                query = query + " WHERE LOWER(md.medicine_name) LIKE LOWER('%{}%')".format(filter["medicine_name"])
                print(query)
        query = query + " ORDER BY pd.created_date DESC"
        return PurchaseDetails.objects.raw(query)


class CustomerDetails(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=False,null=False)
    mobile_no = models.BigIntegerField(blank=False,null=False,db_index=True, unique=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "customer_details"