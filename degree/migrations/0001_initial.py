# Generated by Django 2.2.5 on 2021-03-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=100)),
                ('clipart', models.ImageField(blank=True, default='', upload_to='media')),
            ],
        ),
    ]
