# Generated by Django 4.1.5 on 2023-01-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_rename_enddate_leave_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='user',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
