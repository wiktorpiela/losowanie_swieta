# Generated by Django 4.2.7 on 2023-11-08 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_voter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='name',
            new_name='email',
        ),
    ]
