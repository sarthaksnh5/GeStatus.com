# Generated by Django 4.0.6 on 2022-09-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_machineuser_machine_kv_machineuser_machine_phase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineuser',
            name='machine_kv',
            field=models.CharField(default=45, max_length=200),
        ),
        migrations.AlterField(
            model_name='machineuser',
            name='machine_phase',
            field=models.CharField(default=1, max_length=200),
        ),
    ]