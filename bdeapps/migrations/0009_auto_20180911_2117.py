# Generated by Django 2.0.7 on 2018-09-11 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilapp', '0008_auto_20180824_1730'),
        ('bdeapps', '0008_auto_20180911_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='par_utilisateur',
        ),
        migrations.AddField(
            model_name='mission',
            name='par_utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='utilapp.etudiant'),
        ),
    ]
