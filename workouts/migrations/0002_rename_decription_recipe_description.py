# Generated by Django 5.0.1 on 2024-01-15 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='decription',
            new_name='description',
        ),
    ]