# Generated by Django 2.0.1 on 2018-06-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawakhana', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]