# Generated by Django 2.0.1 on 2018-06-20 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dawakhana', '0008_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
