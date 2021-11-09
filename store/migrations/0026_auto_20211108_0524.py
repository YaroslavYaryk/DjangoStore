# Generated by Django 3.2.8 on 2021-11-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20211107_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoupon',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usersearchhistory',
            name='user',
        ),
        migrations.AddField(
            model_name='usercoupon',
            name='ip',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usersearchhistory',
            name='ip',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]