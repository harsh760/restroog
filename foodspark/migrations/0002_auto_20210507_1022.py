# Generated by Django 3.2.2 on 2021-05-07 10:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodspark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryBoy',
            fields=[
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='deliverystatus',
            field=models.CharField(choices=[('p', 'Pending'), ('d', 'Delivered'), ('a', 'Accepted')], default='p', max_length=1),
        ),
        migrations.CreateModel(
            name='DeliveryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryboy_id', models.EmailField(default='', max_length=254, null=True)),
                ('deliverystatus', models.CharField(choices=[('p', 'Pending'), ('d', 'Delivered'), ('a', 'Accepted')], default='p', max_length=1)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodspark.order')),
            ],
        ),
    ]
