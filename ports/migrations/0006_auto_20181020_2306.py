# Generated by Django 2.1.2 on 2018-10-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ports', '0005_auto_20181020_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='lat',
            field=models.DecimalField(decimal_places=10, max_digits=13),
        ),
        migrations.AlterField(
            model_name='port',
            name='lng',
            field=models.DecimalField(decimal_places=10, max_digits=13),
        ),
    ]