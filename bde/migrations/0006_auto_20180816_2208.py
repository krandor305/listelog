# Generated by Django 2.0.7 on 2018-08-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bde', '0005_auto_20180814_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='image',
            field=models.ImageField(default='default.png', upload_to='imagesetudiant'),
        ),
    ]
