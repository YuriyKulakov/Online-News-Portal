# Generated by Django 2.2.4 on 2019-10-10 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('phonenumber', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
