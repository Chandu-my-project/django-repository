# Generated by Django 2.2.5 on 2021-03-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0014_auto_20210227_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutes',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
