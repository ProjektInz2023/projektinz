# Generated by Django 4.2.6 on 2023-11-21 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0013_alter_order_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='role',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
