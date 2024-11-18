# Generated by Django 5.1 on 2024-09-03 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayedTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('played_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]