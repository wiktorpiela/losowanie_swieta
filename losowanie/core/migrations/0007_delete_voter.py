# Generated by Django 4.2.7 on 2023-11-08 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_chosen_person_name_voter_chosen_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Voter',
        ),
    ]