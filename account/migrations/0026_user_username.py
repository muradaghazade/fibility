# Generated by Django 3.1.6 on 2021-04-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]