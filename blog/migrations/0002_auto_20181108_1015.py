# Generated by Django 2.1.3 on 2018-11-08 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publisded_time',
            new_name='published_date',
        ),
    ]
