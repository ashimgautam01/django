# Generated by Django 5.2.1 on 2025-06-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_post_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
