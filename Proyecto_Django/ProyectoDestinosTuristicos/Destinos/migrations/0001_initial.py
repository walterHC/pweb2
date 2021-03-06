# Generated by Django 3.0.7 on 2020-06-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCiudad', models.CharField(max_length=50)),
                ('descripcionCiudad', models.TextField()),
                ('imagenCiudad', models.ImageField(upload_to='pics')),
                ('precioTour', models.IntegerField()),
                ('ofertaTour', models.BooleanField(default=False)),
            ],
        ),
    ]
