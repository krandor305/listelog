# Generated by Django 2.0.7 on 2018-10-11 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0014_news'),
        ('bdeapps', '0011_newsasso'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsasso',
            name='bde',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='bde.bde'),
            preserve_default=False,
        ),
    ]