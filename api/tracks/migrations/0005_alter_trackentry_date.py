# Generated by Django 3.2.5 on 2022-08-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_alter_trackentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackentry',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
