# Generated by Django 4.2.9 on 2024-01-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(related_name='skill', to='main.skill'),
        ),
    ]
