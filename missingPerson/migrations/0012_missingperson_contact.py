# Generated by Django 4.0.2 on 2022-05-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingPerson', '0011_alter_missingperson_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='contact',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
