# Generated by Django 4.0 on 2022-01-11 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        ('estados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=200)),
                ('fechaPedido', models.DateField(auto_now_add=True)),
                ('horaPedido', models.TimeField(auto_now=True)),
                ('cantidad', models.IntegerField()),
                ('valorTotal', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('telefonoCliente', models.CharField(max_length=200)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articulos.articulo')),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='estados.estado')),
            ],
            options={
                'db_table': 'pedidos_pedido',
            },
        ),
    ]