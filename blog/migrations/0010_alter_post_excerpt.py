# Generated by Django 3.2.20 on 2023-07-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
