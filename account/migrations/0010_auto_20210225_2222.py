# Generated by Django 3.1.6 on 2021-02-25 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='themessage', to='account.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='message', to='account.user'),
            preserve_default=False,
        ),
    ]