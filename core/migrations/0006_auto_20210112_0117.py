# Generated by Django 3.1.5 on 2021-01-12 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210111_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
