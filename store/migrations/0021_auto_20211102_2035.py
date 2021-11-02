# Generated by Django 3.2.8 on 2021-11-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_usercoupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoupon',
            name='coupon_code',
        ),
        migrations.AddField(
            model_name='usercoupon',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.coupon', verbose_name='Coupon'),
        ),
    ]