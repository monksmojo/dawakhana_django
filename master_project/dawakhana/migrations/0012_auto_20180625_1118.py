# Generated by Django 2.0.1 on 2018-06-25 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawakhana', '0011_auto_20180621_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='salt',
            name='s_quantity',
            field=models.CharField(default=' ', max_length=250, verbose_name='Salt Name'),
        ),
        migrations.AlterField(
            model_name='salt',
            name='medicine',
            field=models.ManyToManyField(related_query_name='salt', to='dawakhana.Medicine'),
        ),
    ]
