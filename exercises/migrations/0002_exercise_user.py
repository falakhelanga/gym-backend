# Generated by Django 5.1 on 2024-09-15 06:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='exercises', to=settings.AUTH_USER_MODEL),
        ),
    ]
