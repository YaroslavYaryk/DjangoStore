# Generated by Django 4.0.6 on 2022-07-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_productcomment_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCommentPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='photos/Data%y/%m/%d/', verbose_name='images')),
            ],
        ),
        migrations.AddField(
            model_name='productcomment',
            name='cons',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='pros',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='photos',
            field=models.ManyToManyField(blank=True, to='store.productcommentphotos', verbose_name='commentPhotos'),
        ),
    ]