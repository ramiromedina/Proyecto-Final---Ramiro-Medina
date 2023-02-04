# Generated by Django 4.1.5 on 2023-02-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funkos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('informacion', models.CharField(max_length=600)),
                ('imagenFunko', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Remeras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('talle', models.CharField(max_length=30)),
                ('imagenRemera', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tazas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('informacion', models.CharField(max_length=600)),
                ('colores', models.CharField(max_length=30)),
                ('imagenTaza', models.CharField(max_length=500)),
            ],
        ),
    ]