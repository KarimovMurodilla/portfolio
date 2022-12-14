# Generated by Django 4.0.6 on 2022-09-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_career_end_alter_career_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='works', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
            },
        ),
        migrations.AlterField(
            model_name='career',
            name='end',
            field=models.DateField(verbose_name='Finish date'),
        ),
        migrations.AlterField(
            model_name='career',
            name='start',
            field=models.DateField(verbose_name='Starts From Date'),
        ),
    ]
