# Generated by Django 4.1.2 on 2023-01-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
