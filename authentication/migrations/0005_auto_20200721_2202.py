# Generated by Django 3.0.8 on 2020-07-21 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0004_auto_20200721_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_type', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]