# Generated by Django 2.2.5 on 2020-10-31 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cliente_colaborador_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(max_length=3)),
                ('direccion_entrega', models.CharField(blank=True, max_length=100, null=True)),
                ('tarifa', models.FloatField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cliente')),
                ('repartidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Colaborador')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Producto')),
            ],
        ),
    ]