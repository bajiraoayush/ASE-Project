# Generated by Django 2.1.3 on 2018-12-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_auto_20181202_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='State',
            field=models.CharField(choices=[('Karnataka', 'Karnataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Delhi', 'Delhi'), ('West Bengal', 'West Bengal')], max_length=250),
        ),
    ]
