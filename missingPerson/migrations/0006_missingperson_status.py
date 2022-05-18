# Generated by Django 4.0.2 on 2022-04-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingPerson', '0005_alter_missingperson_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='status',
            field=models.CharField(choices=[('F', 'Found'), ('M', 'Missing')], default='M', max_length=1),
        ),
    ]