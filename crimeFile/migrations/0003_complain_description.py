# Generated by Django 4.0.2 on 2022-02-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeFile', '0002_complain_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='description',
            field=models.TextField(default="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."),
            preserve_default=False,
        ),
    ]