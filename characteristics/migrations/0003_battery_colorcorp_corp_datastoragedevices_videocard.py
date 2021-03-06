# Generated by Django 3.2.8 on 2021-10-25 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0002_auto_20211025_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColorCorp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='DataStorageDevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hard_drive_capacity', models.IntegerField()),
                ('hard_drive_type', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_card', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Corp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('manipulators', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('corp_material', models.CharField(max_length=100)),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characteristics.battery', verbose_name='Battery')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characteristics.colorcorp', verbose_name='ColorCorp')),
            ],
        ),
    ]
