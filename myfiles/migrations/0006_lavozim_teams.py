# Generated by Django 4.0.5 on 2022-12-27 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_remove_teams_lavozim_delete_lavozim_delete_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lavozim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('familya', models.CharField(max_length=20)),
                ('yosh', models.IntegerField()),
                ('rasm', models.ImageField(upload_to='media')),
                ('telegram', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('lavozim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.lavozim')),
            ],
        ),
    ]
