# Generated by Django 4.2 on 2023-12-16 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
    ]