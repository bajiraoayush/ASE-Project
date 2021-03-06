# Generated by Django 2.1.3 on 2018-12-11 13:58

import django.core.validators
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('Restaurants', '0001_initial'),
        ('Delivery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Address_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Home', models.CharField(max_length=250)),
                ('Street', models.CharField(max_length=250)),
                ('Pin', models.CharField(default=0, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('Cart_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField(null=True, verbose_name=django.core.validators.MaxValueValidator(5))),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('Item_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Item_Quantity', models.IntegerField(verbose_name=django.core.validators.MaxValueValidator(10))),
                ('Item_Price', models.IntegerField(default=0)),
                ('Item_Food_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Order_Status',
                 models.IntegerField(null=True, verbose_name=django.core.validators.MaxValueValidator(5))),
                ('Order_Time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('Order_Total_Price', models.IntegerField(default=0, null=True)),
                ('Order_Address',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Customers.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Customer_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Customer_First_Name', models.CharField(max_length=200)),
                ('Customer_Last_Name', models.CharField(max_length=200)),
                ('Customer_Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=13)),
                ('Customer_Picture', models.ImageField(default='media/default_res.jpg', upload_to='media')),
                ('Customer_Email', models.EmailField(default='asd@rew.com', max_length=254)),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Order_Customer_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Customers.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='Order_Delivery_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Delivery.Delivery'),
        ),
        migrations.AddField(
            model_name='order',
            name='Order_Restaurant_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='Restaurants.Restaurant'),
        ),
        migrations.AddField(
            model_name='item',
            name='Item_Order_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Customers.Order'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='Cart_Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.Profile'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='Cart_Food_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurants.Food'),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.Profile'),
        ),
        migrations.AddField(
            model_name='address',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Customers.Area'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Customers.City'),
        ),
    ]
