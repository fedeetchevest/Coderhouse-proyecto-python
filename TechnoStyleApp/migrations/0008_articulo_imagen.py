# Generated by Django 4.2.1 on 2023-07-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TechnoStyleApp", "0007_delete_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="articulo",
            name="imagen",
            field=models.ImageField(default="imagen", upload_to="imagenes/"),
        ),
    ]
