# Generated by Django 3.1.2 on 2020-10-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201017_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='capacity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
