# Generated by Django 3.0.8 on 2020-07-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20200722_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankstatement',
            name='category',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
