# Generated by Django 5.1.5 on 2025-02-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_profile_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='comment',
            field=models.CharField(default='nothing', max_length=70),
        ),
    ]
