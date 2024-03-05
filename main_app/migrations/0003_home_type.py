# Generated by Django 4.2.10 on 2024-03-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_home_lotsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='type',
            field=models.CharField(choices=[('house', 'House'), ('lot', 'Lot'), ('multifamily', 'Multi-family'), ('condo', 'Condominium'), ('townhomes', 'Townhomes')], default='house', max_length=50),
        ),
    ]
