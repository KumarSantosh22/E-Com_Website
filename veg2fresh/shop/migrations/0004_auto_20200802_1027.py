# Generated by Django 3.0.8 on 2020-08-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200802_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]
