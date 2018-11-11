# Generated by Django 2.0.6 on 2018-11-11 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Customer_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Customer_FName', models.CharField(max_length=200)),
                ('Customer_LName', models.CharField(max_length=200)),
                ('Customer_Num', models.CharField(max_length=10, unique=True)),
                ('Customer_Pic', models.ImageField(upload_to='Customers/Pictures/Profiles')),
                ('Customer_Email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.Profile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Order_Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.Profile'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]