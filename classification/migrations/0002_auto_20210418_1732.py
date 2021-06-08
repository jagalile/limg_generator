# Generated by Django 3.1.7 on 2021-04-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='label',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='image',
            name='review',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
