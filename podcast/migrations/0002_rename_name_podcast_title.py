# Generated by Django 5.0.7 on 2024-08-02 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcast',
            old_name='name',
            new_name='title',
        ),
    ]