# Generated by Django 4.2.2 on 2023-06-27 03:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('elevator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingconfiguration',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'UP'), (2, 'DOWN'), (3, 'STOP'), (4, 'MAINTENANCE')], default=1)),
                ('door_status', models.IntegerField(choices=[(1, 'CLOSE'), (2, 'OPEN')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elevator.buildingconfiguration')),
            ],
        ),
    ]
