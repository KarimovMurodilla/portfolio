# Generated by Django 4.0.6 on 2023-06-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_works_alter_career_end_alter_career_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
