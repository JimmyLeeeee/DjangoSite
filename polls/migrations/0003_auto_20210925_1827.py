# Generated by Django 3.2.7 on 2021-09-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_thought'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deepthoughts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Thought',
        ),
    ]
