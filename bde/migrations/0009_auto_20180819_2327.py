# Generated by Django 2.0.7 on 2018-08-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0008_bde_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bde',
            name='nom',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]