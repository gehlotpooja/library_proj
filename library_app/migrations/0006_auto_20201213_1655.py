# Generated by Django 3.1.4 on 2020-12-13 11:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_auto_20201212_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissue',
            name='issue_date',
            field=models.DateField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
