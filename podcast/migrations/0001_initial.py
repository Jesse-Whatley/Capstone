# Generated by Django 5.0.7 on 2024-07-31 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/img')),
                ('link', models.URLField()),
            ],
        ),
    ]
