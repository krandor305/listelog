# Generated by Django 2.0.7 on 2018-08-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bde', '0010_auto_20180820_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messagebde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField(max_length=2000)),
                ('bdec', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bde.bde')),
            ],
        ),
    ]
