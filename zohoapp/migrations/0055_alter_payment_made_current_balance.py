# Generated by Django 3.2.20 on 2023-11-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0054_auto_20231125_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_made',
            name='current_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
