# Generated by Django 3.2.9 on 2021-12-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=100)),
                ('updated_at', models.CharField(max_length=100)),
            ],
        ),
    ]
