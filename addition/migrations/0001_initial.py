# Generated by Django 4.0.3 on 2022-03-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
                ('answer', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]