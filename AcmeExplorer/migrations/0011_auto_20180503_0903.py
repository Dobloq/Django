# Generated by Django 2.0.4 on 2018-05-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcmeExplorer', '0010_auto_20180503_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parentCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='AcmeExplorer.Category'),
        ),
    ]