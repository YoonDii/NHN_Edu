# Generated by Django 3.2.13 on 2023-01-23 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchlist',
            old_name='boby',
            new_name='body',
        ),
        migrations.AlterModelTable(
            name='searchlist',
            table='search_list',
        ),
    ]