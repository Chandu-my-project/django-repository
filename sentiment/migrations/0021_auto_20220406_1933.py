# Generated by Django 2.2.5 on 2022-04-06 14:03

import django.core.validators
from django.db import migrations, models
import sentiment.models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0020_remove_course_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='grad_year',
            field=models.PositiveIntegerField(default=2022, null=True, validators=[django.core.validators.MinValueValidator(1985), sentiment.models.max_value_current_year]),
        ),
    ]
