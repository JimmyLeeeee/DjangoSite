# Generated by Django 3.2.7 on 2021-09-26 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210925_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deepthoughts',
            name='title',
        ),
    ]