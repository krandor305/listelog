# Generated by Django 2.0.7 on 2018-09-11 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdeapps', '0009_auto_20180911_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='par_utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilapp.etudiant'),
        ),
    ]
