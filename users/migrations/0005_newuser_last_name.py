# Generated by Django 4.0.6 on 2022-09-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_user_name_newuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]