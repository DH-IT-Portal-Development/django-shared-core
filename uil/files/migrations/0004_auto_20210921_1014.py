# Generated by Django 3.2.6 on 2021-09-21 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_file_field_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='app_name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='field_name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='model_name',
        ),
    ]
