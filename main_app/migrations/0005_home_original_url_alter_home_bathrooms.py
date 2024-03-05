# Generated by Django 4.2.10 on 2024-03-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_home_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='original_url',
            field=models.URLField(default='https://www.zillow.com/homedetails/20-Dogwood-Ln-Briarcliff-Manor-NY-10510/109900201_zpid/', max_length=255, verbose_name='Original URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='home',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]