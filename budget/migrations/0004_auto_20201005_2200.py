# Generated by Django 3.0.7 on 2020-10-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_months_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='months',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
