# Generated by Django 4.2.6 on 2023-11-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alergen_maincourse_alergens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mainCourse',
            field=models.ForeignKey(null=True, on_delete=models.SET('Danie usuniete'), to='api.maincourse'),
        ),
    ]