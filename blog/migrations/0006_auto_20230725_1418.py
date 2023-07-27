# Generated by Django 3.2.20 on 2023-07-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20230725_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Post')], default=True),
        ),
    ]