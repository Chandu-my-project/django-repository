# Generated by Django 2.2.5 on 2021-02-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210212_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='combo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='combo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
