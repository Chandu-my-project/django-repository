# Generated by Django 2.2.5 on 2021-03-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree', '0009_auto_20210326_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
