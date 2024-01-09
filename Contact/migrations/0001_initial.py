# Generated by Django 4.2.5 on 2023-10-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=40)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]
