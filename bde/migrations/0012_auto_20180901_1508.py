# Generated by Django 2.0.7 on 2018-09-01 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0011_auto_20180824_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bdeappartenant',
        ),
        migrations.DeleteModel(
            name='event',
        ),
    ]