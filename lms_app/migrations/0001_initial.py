# Generated by Django 4.2 on 2023-08-12 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='posts/')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('retal_price_day', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('retal_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('rented', 'rented'), ('sold', 'sold')], max_length=50, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lms_app.category')),
            ],
        ),
    ]
