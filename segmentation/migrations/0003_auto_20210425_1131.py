# Generated by Django 3.1.7 on 2021-04-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segmentation', '0002_auto_20210425_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmentationimage',
            name='img',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
