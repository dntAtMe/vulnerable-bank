# Generated by Django 2.1.4 on 2019-01-10 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=1),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 13, 21, 55, 972257)),
        ),
    ]