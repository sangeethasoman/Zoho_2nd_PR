# Generated by Django 3.2.20 on 2023-09-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0007_auto_20230923_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='document',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='status',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='title',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.AlterField(
            model_name='expense',
            name='activation_tag',
            field=models.CharField(default='active', max_length=20),
        ),
    ]
