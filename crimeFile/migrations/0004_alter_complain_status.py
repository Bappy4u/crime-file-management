# Generated by Django 4.0.2 on 2022-02-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeFile', '0003_complain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('I', 'Investigating'), ('D', 'Dismissed')], default='P', max_length=2),
        ),
    ]
