# Generated by Django 4.1.1 on 2022-09-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='truncated_url',
            field=models.CharField(max_length=5000),
        ),
    ]