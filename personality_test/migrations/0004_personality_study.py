# Generated by Django 2.2.5 on 2021-04-02 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personality_test', '0003_delete_personality_study'),
    ]

    operations = [
        migrations.CreateModel(
            name='personality_study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(max_length=100)),
                ('study_des', models.CharField(max_length=5000)),
                ('peronality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personality_test.personality')),
            ],
        ),
    ]
