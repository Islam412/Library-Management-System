# Generated by Django 4.2 on 2023-08-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_alter_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_render',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
    ]