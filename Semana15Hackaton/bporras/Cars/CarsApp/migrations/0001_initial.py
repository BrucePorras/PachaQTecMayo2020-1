# Generated by Django 3.1 on 2020-09-05 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tipo',
                'verbose_name_plural': 'tipos',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('año', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarsApp.marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarsApp.tipo')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
