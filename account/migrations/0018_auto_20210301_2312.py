# Generated by Django 3.1.6 on 2021-03-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210301_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
