# Generated by Django 2.2.4 on 2019-12-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainevent', '0004_auto_20191204_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='ua_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userbehavior',
            name='ub_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
