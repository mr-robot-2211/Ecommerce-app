# Generated by Django 4.2 on 2023-05-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reviews',
            field=models.CharField(default='no reviews yet', max_length=100),
        ),
    ]
