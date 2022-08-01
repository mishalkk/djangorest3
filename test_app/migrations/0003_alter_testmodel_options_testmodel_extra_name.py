# Generated by Django 4.0.6 on 2022-08-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_testmodel_created_at_testmodel_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='extra_name',
            field=models.CharField(default='null', editable=False, max_length=250),
        ),
    ]