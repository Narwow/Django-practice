# Generated by Django 2.0.4 on 2018-04-16 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_poll', '0002_fact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fact',
        ),
    ]
