# Generated by Django 4.2.6 on 2023-11-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_maincourse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincourse',
            name='image',
            field=models.CharField(default=None, max_length=255),
        ),
    ]