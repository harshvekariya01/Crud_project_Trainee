# Generated by Django 4.1.5 on 2023-01-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_leave_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='reason',
            field=models.TextField(default=''),
        ),
    ]
