# Generated by Django 3.2.3 on 2021-10-18 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=20, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='contest_images')),
                ('description', models.CharField(max_length=1000)),
                ('date_of_posting', models.DateField(default=datetime.date.today)),
                ('status', models.TextField(choices=[('active', 'active'), ('closed', 'closed')], default='active')),
            ],
        ),
    ]