# Generated by Django 4.1.4 on 2022-12-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='rarity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fishing',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
