# Generated by Django 4.0.6 on 2022-08-08 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_alter_testmodel_options_modelx'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ModelX',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]