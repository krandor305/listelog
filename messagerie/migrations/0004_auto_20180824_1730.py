# Generated by Django 2.0.7 on 2018-08-24 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messagerie', '0003_auto_20180823_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagebde',
            name='etudiantc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='utilapp.etudiant'),
        ),
    ]