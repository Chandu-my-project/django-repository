# Generated by Django 2.2.5 on 2021-02-25 07:08

import django.core.validators
from django.db import migrations, models
import sentiment.models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0006_feedback_enroll_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='grad_year',
            field=models.PositiveIntegerField(default=2021, null=True, validators=[django.core.validators.MinValueValidator(1985), sentiment.models.max_value_current_year]),
        ),
    ]
