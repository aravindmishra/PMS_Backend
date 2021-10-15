from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300,blank=True,null=True)
    dob = models.DateTimeField(blank=True,null=True)
    mobile_no = models.BigIntegerField(blank=False,null=False)
    email_id = models.CharField(max_length=500,blank=True,null=True)
    status = models.IntegerField(blank=True,null=True)
    created_by = models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(blank=False,null=False)
    modified_by = models.IntegerField(blank=True,null=True)
    modified_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = "user_details"

class LoginHistory(models.Model):
    login_history_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=False,null=False)
    login_time = models.DateTimeField(blank=False,null=False)
    
    class Meta:
        db_table = "login_history"
