# Generated by Django 4.2.6 on 2023-11-25 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_maincourse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincourse',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
