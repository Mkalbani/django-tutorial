# Generated by Django 4.2.3 on 2023-07-25 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tutorialcategory_alter_tutorial_tutorial_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateField(default=datetime.datetime(2023, 7, 25, 11, 10, 40, 94015), verbose_name='date published'),
        ),
    ]
