# Generated by Django 4.2.7 on 2023-11-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_voter_chosen_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='isChosen',
            field=models.BooleanField(default=False),
        ),
    ]