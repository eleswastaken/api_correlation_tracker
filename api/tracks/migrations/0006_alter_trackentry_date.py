# Generated by Django 4.1 on 2022-08-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0005_alter_trackentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackentry',
            name='date',
            field=models.DateField(),
        ),
    ]