# Generated by Django 3.2.9 on 2021-11-22 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0010_alter_layer2_networkid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layer2',
            options={'get_latest_by': 'NetworkID'},
        ),
    ]
