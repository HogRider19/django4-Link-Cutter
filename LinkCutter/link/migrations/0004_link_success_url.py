# Generated by Django 4.1.1 on 2022-09-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_link_transition'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='success_url',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
