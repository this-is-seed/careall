# Generated by Django 2.2.7 on 2020-01-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retired', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='help',
            field=models.BooleanField(default=True),
        ),
    ]