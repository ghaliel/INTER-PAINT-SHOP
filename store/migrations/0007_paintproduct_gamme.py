# Generated by Django 5.2.2 on 2025-06-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_shipping_address_order_shipping_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paintproduct',
            name='gamme',
            field=models.CharField(choices=[('luxe', 'Gamme de Luxe'), ('pro', 'Gamme Pro')], default='pro', max_length=10, verbose_name='Gamme'),
        ),
    ]
