# Generated by Django 4.2.1 on 2023-05-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ads_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='slug',
        ),
        migrations.AlterField(
            model_name='ads',
            name='is_published',
            field=models.CharField(default='None', max_length=6),
        ),
    ]
