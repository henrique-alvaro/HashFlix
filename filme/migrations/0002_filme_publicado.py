# Generated by Django 4.2.2 on 2023-08-10 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]