# Generated by Django 4.2 on 2023-08-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('متاح', 'متاح'), ('متأجر', 'متأجر'), ('متباع', 'متباع')], max_length=50, null=True),
        ),
    ]
