# Generated by Django 4.2.5 on 2023-12-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GenerateCSS', '0003_remove_generatecsshomelinks_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatecsshomelinks',
            name='desc',
            field=models.TextField(),
        ),
    ]
