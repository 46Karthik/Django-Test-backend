# Generated by Django 4.2.5 on 2023-12-16 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_storesong_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user_user',
        ),
    ]
