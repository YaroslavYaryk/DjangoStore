# Generated by Django 4.0.6 on 2022-09-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_alter_order_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='saved',
            field=models.BooleanField(default=False),
        ),
    ]
