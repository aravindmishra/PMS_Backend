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

    def medicineList():
        query = "SELECT distinct(md.medicine_id), md.rack_no, md.medicine_name, md.brand, md.power, md.price, md.quantity , sd.status, (SELECT SUM(purchased_qty) FROM purchase_details  WHERE medicine_id = md.medicine_id GROUP BY medicine_id) AS purchased_qty FROM medicine_details AS md LEFT JOIN purchase_details AS pd ON md.medicine_id = pd.medicine_id INNER JOIN status_details AS sd ON sd.status_id = md.status ORDER BY rack_no ASC"
        return MedicineDetails.objects.raw(query)



class StatusDetails(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        db_table = "status_details"