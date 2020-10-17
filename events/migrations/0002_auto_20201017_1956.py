# Generated by Django 3.1.2 on 2020-10-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='events_attendance', to='events.event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
