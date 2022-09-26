# Generated by Django 4.0.7 on 2022-09-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='systemmessage.message.help_text', verbose_name='systemmessage.message')),
                ('message_nl', models.TextField(help_text='systemmessage.message.help_text', null=True, verbose_name='systemmessage.message')),
                ('message_en', models.TextField(help_text='systemmessage.message.help_text', null=True, verbose_name='systemmessage.message')),
                ('color', models.CharField(choices=[('primary', 'systemmessage.color.primary'), ('secondary', 'systemmessage.color.secondary'), ('success', 'systemmessage.color.success'), ('danger', 'systemmessage.color.danger'), ('warning', 'systemmessage.color.warning'), ('info', 'systemmessage.color.info'), ('light', 'systemmessage.color.light'), ('dark', 'systemmessage.color.dark')], help_text='systemmessage.color.help_text', max_length=15, verbose_name='systemmessage.color')),
                ('not_before', models.DateTimeField(blank=True, help_text='systemmessage.not_before.help_text', null=True, verbose_name='systemmessage.not_before')),
                ('not_after', models.DateTimeField(blank=True, help_text='systemmessage.not_after.help_text', null=True, verbose_name='systemmessage.not_after')),
            ],
        ),
    ]
