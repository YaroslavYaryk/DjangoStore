# Generated by Django 4.0.6 on 2022-07-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_likedcomment_productcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
