# Generated by Django 4.0.3 on 2022-03-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='answer',
            field=models.IntegerField(blank=True),
        ),
    ]
