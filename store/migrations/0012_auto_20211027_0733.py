# Generated by Django 3.2.8 on 2021-10-27 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20211027_0545'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WomanImage',
            new_name='ProductImage',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='post',
            new_name='product',
        ),
    ]
