# Generated by Django 4.1.7 on 2023-05-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('text', models.TextField(verbose_name='Что понравилось / не понравислось?')),
            ],
        ),
    ]
