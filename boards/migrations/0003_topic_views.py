# Generated by Django 2.2.5 on 2020-01-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200107_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
