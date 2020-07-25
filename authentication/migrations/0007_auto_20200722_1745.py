# Generated by Django 3.0.8 on 2020-07-22 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20200722_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankstatement',
            name='bankdetails',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bank_statements', to='authentication.BankDetails'),
        ),
    ]