# Generated by Django 2.2.5 on 2021-02-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210212_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='combo',
        ),
        migrations.RemoveField(
            model_name='student',
            name='major',
        ),
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='combo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='major',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
