# Generated by Django 2.2.5 on 2021-02-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_rev'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='overall_rating',
            field=models.IntegerField(null=True),
        ),
    ]
