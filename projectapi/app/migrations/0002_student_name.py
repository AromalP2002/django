# Generated by Django 5.1.2 on 2024-11-22 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='aromal', max_length=30),
            preserve_default=False,
        ),
    ]