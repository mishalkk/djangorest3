# Generated by Django 4.0.6 on 2022-07-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
