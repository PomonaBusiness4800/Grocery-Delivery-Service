# Generated by Django 3.1.7 on 2021-03-24 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
    ]
