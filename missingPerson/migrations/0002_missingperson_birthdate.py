# Generated by Django 4.0.2 on 2022-03-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingPerson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='birthDate',
            field=models.DateTimeField(null=True),
        ),
    ]
