# Generated by Django 4.2.1 on 2023-06-04 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_staff_group_alter_staff_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='group',
            new_name='role',
        ),
    ]