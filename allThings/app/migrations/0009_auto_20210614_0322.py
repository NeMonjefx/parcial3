# Generated by Django 3.1.2 on 2021-06-14 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210614_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='dv',
            new_name='digito_verificador',
        ),
    ]
