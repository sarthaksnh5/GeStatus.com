# Generated by Django 3.1.3 on 2021-07-16 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0003_auto_20210711_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uielement',
            name='mac',
        ),
        migrations.DeleteModel(
            name='machineVI',
        ),
        migrations.DeleteModel(
            name='uiElement',
        ),
    ]
