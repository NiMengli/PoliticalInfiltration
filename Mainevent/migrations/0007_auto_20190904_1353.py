# Generated by Django 2.2.4 on 2019-09-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainevent', '0006_task_e_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='e_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]