# Generated by Django 4.0.5 on 2022-12-27 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0006_lavozim_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='lavozim',
        ),
        migrations.DeleteModel(
            name='Lavozim',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]