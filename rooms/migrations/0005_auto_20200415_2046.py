# Generated by Django 2.2.5 on 2020-04-15 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200415_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='chekc_out',
            new_name='check_out',
        ),
    ]