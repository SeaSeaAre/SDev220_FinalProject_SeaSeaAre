# Generated by Django 4.0.3 on 2023-07-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('ssn', models.CharField(max_length=9)),
                
            ],
        ),
    ]
