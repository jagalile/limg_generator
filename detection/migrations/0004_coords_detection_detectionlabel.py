# Generated by Django 3.1.7 on 2021-04-25 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_auto_20210425_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectionLabel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detection.detectionimage')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detection.detectionlabel')),
            ],
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('x1', models.FloatField()),
                ('y1', models.FloatField()),
                ('x2', models.FloatField()),
                ('y2', models.FloatField()),
                ('detection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detection.detection')),
            ],
        ),
    ]
