# Generated by Django 5.0.1 on 2024-06-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.DateTimeField()),
                ('people', models.IntegerField()),
                ('specialnote', models.CharField(max_length=70)),
            ],
        ),
    ]
