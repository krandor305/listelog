# Generated by Django 2.0.7 on 2018-08-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0009_auto_20180819_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='bde',
            name='adresse',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bde',
            name='etablissement',
            field=models.CharField(default=56, max_length=60),
            preserve_default=False,
        ),
    ]