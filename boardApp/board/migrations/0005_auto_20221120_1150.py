# Generated by Django 3.2 on 2022-11-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20221120_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='いいね'),
        ),
        migrations.AlterField(
            model_name='post',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='既読者数'),
        ),
    ]
