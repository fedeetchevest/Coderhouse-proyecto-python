# Generated by Django 4.2.1 on 2023-06-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TechnoStyleApp", "0004_clientes_sucursales"),
    ]

    operations = [
        migrations.AddField(
            model_name="articulo",
            name="descripcion",
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
