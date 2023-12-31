# Generated by Django 4.0.3 on 2023-07-29 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppV2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='ssn',
        ),
        migrations.AddField(
            model_name='client',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='client',
            name='message',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='received_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Read', 'Read')], default='Pending', max_length=15),
        ),
        migrations.AddField(
            model_name='client',
            name='subject',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
