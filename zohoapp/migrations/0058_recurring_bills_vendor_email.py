# Generated by Django 4.2.6 on 2023-12-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0057_payment_made_sum_amount_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurring_bills',
            name='vendor_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
