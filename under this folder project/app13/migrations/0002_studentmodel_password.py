# Generated by Django 3.0.1 on 2020-03-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app13', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='password',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
