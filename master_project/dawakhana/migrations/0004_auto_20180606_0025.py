# Generated by Django 2.0.1 on 2018-06-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawakhana', '0003_auto_20180605_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
