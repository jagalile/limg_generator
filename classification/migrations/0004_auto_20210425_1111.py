# Generated by Django 3.1.7 on 2021-04-25 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0003_auto_20210418_1737'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ClassificationImage',
        ),
    ]
