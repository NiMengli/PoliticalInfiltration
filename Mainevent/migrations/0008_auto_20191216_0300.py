# Generated by Django 2.2.4 on 2019-12-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainevent', '0007_auto_20191208_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='figure',
            field=models.ManyToManyField(related_name='enent', to='Mainevent.Figure'),
        ),
        migrations.AlterField(
            model_name='event',
            name='information',
            field=models.ManyToManyField(related_name='enent', to='Mainevent.Information'),
        ),
    ]
