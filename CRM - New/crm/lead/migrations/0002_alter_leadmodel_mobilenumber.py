# Generated by Django 5.0.1 on 2024-03-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadmodel',
            name='mobileNumber',
            field=models.CharField(max_length=100),
        ),
    ]
