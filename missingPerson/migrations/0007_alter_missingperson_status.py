# Generated by Django 4.0.2 on 2022-05-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingPerson', '0006_missingperson_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='status',
            field=models.CharField(choices=[('FOUND', 'Found'), ('MISSING', 'Missing')], default='MISSING', max_length=7),
        ),
    ]
