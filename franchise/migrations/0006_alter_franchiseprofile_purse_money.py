# Generated by Django 5.0.1 on 2024-05-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchise', '0005_alter_franchiseprofile_purse_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchiseprofile',
            name='purse_money',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=20),
        ),
    ]
