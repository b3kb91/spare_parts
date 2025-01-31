# Generated by Django 5.0.6 on 2024-11-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_is_staff"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="is_new",
            field=models.BooleanField(default=False, verbose_name="Новый"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_new",
            field=models.BooleanField(default=True, verbose_name="Новый"),
        ),
    ]
