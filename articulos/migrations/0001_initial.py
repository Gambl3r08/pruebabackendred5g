# Generated by Django 4.0 on 2022-01-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('valor', models.IntegerField()),
            ],
            options={
                'db_table': 'articulos_articulo',
            },
        ),
    ]
