# Generated by Django 3.2.8 on 2021-10-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0007_auto_20211026_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='processortype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='processor type'),
        ),
    ]
