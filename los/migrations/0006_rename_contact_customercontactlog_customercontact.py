# Generated by Django 3.2.8 on 2022-02-14 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('los', '0005_auto_20220214_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customercontactlog',
            old_name='contact',
            new_name='customercontact',
        ),
    ]
