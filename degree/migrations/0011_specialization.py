# Generated by Django 2.2.5 on 2021-04-13 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('degree', '0010_auto_20210326_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special', models.CharField(max_length=100)),
                ('discipline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='degree.Discipline')),
            ],
        ),
    ]
