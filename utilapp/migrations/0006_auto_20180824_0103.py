# Generated by Django 2.0.7 on 2018-08-23 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilapp', '0005_auto_20180824_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membrebde',
            name='bdechoisi',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='bde.bde'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membrebde',
            name='poste',
            field=models.CharField(blank=True, choices=[('President', 'President'), ('Tresorier', 'Tresorier'), ('Membre', 'Membre')], default=2, max_length=15),
            preserve_default=False,
        ),
    ]
