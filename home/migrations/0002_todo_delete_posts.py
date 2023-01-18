# Generated by Django 4.1.2 on 2023-01-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('Description', models.TextField()),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], default='pending', max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='posts',
        ),
    ]
