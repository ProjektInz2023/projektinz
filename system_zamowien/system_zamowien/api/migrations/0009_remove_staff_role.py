# Generated by Django 4.2.1 on 2023-10-22 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='role',
        ),
    ]
