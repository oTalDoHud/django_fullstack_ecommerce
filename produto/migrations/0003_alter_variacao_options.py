# Generated by Django 4.2 on 2023-04-22 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0002_variacao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="variacao",
            options={"verbose_name": "Variação", "verbose_name_plural": "Variações"},
        ),
    ]