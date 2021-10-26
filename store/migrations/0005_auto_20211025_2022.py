# Generated by Django 3.2.8 on 2021-10-25 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0004_connection_countrybrand_countrymade_producttype'),
        ('store', '0004_auto_20211025_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='connection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characteristics.connection', verbose_name='Connection'),
        ),
        migrations.AddField(
            model_name='product',
            name='country_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characteristics.countrybrand', verbose_name='CountryBrand'),
        ),
        migrations.AddField(
            model_name='product',
            name='country_made',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characteristics.countrymade', verbose_name='CountryMade'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type_of_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='characteristics.producttype', verbose_name='ProductType'),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/Data%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.IntegerField(null=True),
        ),
    ]
