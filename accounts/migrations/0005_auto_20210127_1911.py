# Generated by Django 3.1.4 on 2021-01-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210127_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
