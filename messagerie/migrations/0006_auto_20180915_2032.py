# Generated by Django 2.0.7 on 2018-09-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagerie', '0005_messageanon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageanon',
            name='bdec',
        ),
        migrations.AddField(
            model_name='messagebde',
            name='anonymat',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Messageanon',
        ),
    ]
