# Generated by Django 2.0.4 on 2018-04-20 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcmeExplorer', '0003_auto_20180420_0035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrator',
            options={'permissions': (('ADMINISTRATOR', 'Permission for administrator'),)},
        ),
        migrations.AlterModelOptions(
            name='auditor',
            options={'permissions': (('AUDITOR', 'Permission for auditor'),)},
        ),
        migrations.AlterModelOptions(
            name='explorer',
            options={'permissions': (('EXPLORER', 'Permission for explorer'),)},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'permissions': (('MANAGER', 'Permission for manager'),)},
        ),
        migrations.AlterModelOptions(
            name='ranger',
            options={'permissions': (('RANGER', 'Permission for ranger'),)},
        ),
        migrations.AlterModelOptions(
            name='sponsor',
            options={'permissions': (('SPONSOR', 'Permission for sponsor'),)},
        ),
    ]