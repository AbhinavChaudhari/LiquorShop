# Generated by Django 3.1.1 on 2020-10-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_purchase_bottols'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='bottols',
            field=models.IntegerField(default='0'),
        ),
    ]
