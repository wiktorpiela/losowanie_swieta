# Generated by Django 4.2.7 on 2023-11-08 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_voter_chosen_person_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='chosen_person_name',
            new_name='chosen_person',
        ),
    ]