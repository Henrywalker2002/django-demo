# Generated by Django 4.2.2 on 2023-06-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(help_text='example : 2023'),
        ),
    ]