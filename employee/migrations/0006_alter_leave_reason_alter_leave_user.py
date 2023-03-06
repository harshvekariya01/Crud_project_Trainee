# Generated by Django 4.1.5 on 2023-01-27 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_remove_leave_total_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]