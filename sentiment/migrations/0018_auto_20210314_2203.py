# Generated by Django 2.2.5 on 2021-03-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0017_auto_20210314_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='neg',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='neu',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='pos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
