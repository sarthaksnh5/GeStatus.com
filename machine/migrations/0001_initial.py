# Generated by Django 3.1.3 on 2021-07-11 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='uiElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField()),
                ('coolant', models.IntegerField()),
                ('oilTemp', models.IntegerField()),
                ('voltage', models.FloatField()),
                ('fuel', models.FloatField()),
                ('oilPress', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='machineVI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vr', models.FloatField()),
                ('vy', models.FloatField()),
                ('vb', models.FloatField()),
                ('vry', models.FloatField()),
                ('vyb', models.FloatField()),
                ('vbr', models.FloatField()),
                ('ir', models.FloatField()),
                ('iy', models.FloatField()),
                ('ib', models.FloatField()),
                ('pf', models.FloatField()),
                ('power', models.FloatField()),
                ('kwh', models.FloatField()),
                ('trhr', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('deviceno', models.CharField(max_length=200)),
                ('genset_no', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('time_at', models.TimeField(auto_now_add=True)),
                ('low_oil', models.BooleanField(default=False)),
                ('high_engine', models.BooleanField(default=False)),
                ('low_fuel', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
