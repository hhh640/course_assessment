# Generated by Django 3.1.5 on 2021-01-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='sfzx',
            field=models.BooleanField(default=False, help_text='是否在校'),
        ),
    ]
