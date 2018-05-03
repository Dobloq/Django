# Generated by Django 2.0.4 on 2018-05-02 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AcmeExplorer', '0007_auto_20180421_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parentFolder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AcmeExplorer.Folder'),
        ),
    ]
