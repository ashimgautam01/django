# Generated by Django 5.2.1 on 2025-06-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
