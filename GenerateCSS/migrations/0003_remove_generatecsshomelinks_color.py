# Generated by Django 4.2.5 on 2023-12-16 10:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('GenerateCSS', '0002_generatecsshomelinks_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatecsshomelinks',
            name='color',
        ),
    ]
