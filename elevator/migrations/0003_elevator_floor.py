# Generated by Django 4.2.2 on 2023-06-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator', '0002_alter_buildingconfiguration_id_elevator'),
    ]

    operations = [
        migrations.AddField(
            model_name='elevator',
            name='floor',
            field=models.IntegerField(default=0),
        ),
    ]