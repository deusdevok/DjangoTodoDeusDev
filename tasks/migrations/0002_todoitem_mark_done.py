# Generated by Django 4.2.5 on 2023-10-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='mark_done',
            field=models.BooleanField(default=False),
        ),
    ]
