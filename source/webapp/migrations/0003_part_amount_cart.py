# Generated by Django 5.0.6 on 2024-09-11 10:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0002_alter_carbrand_options_alter_carmodel_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="part",
            name="amount",
            field=models.PositiveIntegerField(default=0, verbose_name="Остаток"),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=1,
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carts",
                        to="webapp.part",
                        verbose_name="запчасти",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар в корзине",
                "verbose_name_plural": "Товары в корзине",
                "db_table": "cart",
            },
        ),
    ]
