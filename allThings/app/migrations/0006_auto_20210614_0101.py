# Generated by Django 3.1.2 on 2021-06-14 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210613_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
