# Generated by Django 2.2.5 on 2021-03-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree', '0007_auto_20210326_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='career_des',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='description',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]
