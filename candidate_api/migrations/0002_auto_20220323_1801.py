# Generated by Django 3.1.14 on 2022-03-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
