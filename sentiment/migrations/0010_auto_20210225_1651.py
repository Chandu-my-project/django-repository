# Generated by Django 2.2.5 on 2021-02-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0009_auto_20210225_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='star1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='star2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='star3',
            field=models.IntegerField(null=True),
        ),
    ]
