# Generated by Django 3.2.9 on 2021-11-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0005_billdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
            name='bill_data',
            field=models.JSONField(),
        ),
    ]