# Generated by Django 2.0.7 on 2018-10-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_section_bde'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='url',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
