# Generated by Django 4.1.6 on 2023-02-07 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0002_remove_thought_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
