# Generated by Django 4.2.6 on 2023-12-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0060_recurring_bills_place_of_supply'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasebills',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
