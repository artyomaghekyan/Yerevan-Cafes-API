# Generated by Django 4.1.7 on 2023-02-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
