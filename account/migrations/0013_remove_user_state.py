# Generated by Django 3.1.6 on 2021-02-27 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210227_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
    ]
