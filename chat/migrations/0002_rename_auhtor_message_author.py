# Generated by Django 5.0.8 on 2024-08-08 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='auhtor',
            new_name='author',
        ),
    ]
