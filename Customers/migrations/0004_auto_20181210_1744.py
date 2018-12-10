# Generated by Django 2.1.3 on 2018-12-10 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_auto_20181202_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Order_Address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Customers.Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Customer_Picture',
            field=models.ImageField(default='media/default_res.jpg', upload_to='media'),
        ),
    ]
