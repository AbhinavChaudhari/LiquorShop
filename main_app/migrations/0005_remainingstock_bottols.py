# Generated by Django 3.1.1 on 2020-10-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_saletrans_bottols'),
    ]

    operations = [
        migrations.AddField(
            model_name='remainingstock',
            name='bottols',
            field=models.IntegerField(default='0'),
        ),
    ]
