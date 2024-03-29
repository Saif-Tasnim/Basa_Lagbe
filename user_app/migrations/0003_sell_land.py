# Generated by Django 4.1.7 on 2023-03-03 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0002_sell_flat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell_land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.TextField(blank=True, max_length=255, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('ammount', models.CharField(blank=True, max_length=50, null=True)),
                ('plots_count', models.IntegerField(blank=True, null=True)),
                ('land_type', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('land_image', models.ImageField(blank=True, null=True, upload_to='land_photos')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
