# Generated by Django 2.1.2 on 2018-10-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181020_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_portorg',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]