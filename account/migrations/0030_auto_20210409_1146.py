# Generated by Django 3.1.6 on 2021-04-09 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_auto_20210409_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='end_budget',
        ),
        migrations.RemoveField(
            model_name='user',
            name='start_budget',
        ),
        migrations.DeleteModel(
            name='EndBudget',
        ),
        migrations.DeleteModel(
            name='StartBudget',
        ),
    ]