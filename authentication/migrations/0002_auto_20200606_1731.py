# Generated by Django 3.0.7 on 2020-06-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='publict_entity',
            new_name='public_entity',
        ),
    ]