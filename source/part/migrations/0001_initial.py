# Generated by Django 5.0.6 on 2024-10-13 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webapp', '0019_remove_orderpart_order_remove_orderpart_part_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Остаток')),
                ('image1', models.ImageField(default='default.jpg', upload_to='parts/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='parts/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='parts/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='webapp.category')),
                ('vehicle_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='webapp.vehicleinfo')),
            ],
            options={
                'verbose_name': 'Запчасть',
                'verbose_name_plural': 'Запчасти',
                'db_table': 'car_part',
            },
        ),
    ]
