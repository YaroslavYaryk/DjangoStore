# Generated by Django 4.0.6 on 2022-09-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0009_auto_20211027_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='category/Data%y/%m/%d/'),
        ),
    ]
