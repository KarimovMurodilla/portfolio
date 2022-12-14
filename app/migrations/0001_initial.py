# Generated by Django 4.0.6 on 2022-08-27 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_name', models.CharField(max_length=20, verbose_name='Name')),
                ('short_desription', models.CharField(max_length=150, verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('start', models.DateField(verbose_name='Starts From Date')),
                ('end', models.DateField(verbose_name='Finish date')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('start', models.DateField(verbose_name='Starts From Date')),
                ('end', models.DateField(verbose_name='Finish date')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clients', verbose_name='Client Images')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('level', models.PositiveIntegerField(default=0, help_text='set your level', verbose_name='Level')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('my_skills', models.ManyToManyField(related_name='my_skills', to='app.programmingskills', verbose_name='skills')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('gmail', models.CharField(max_length=50, verbose_name='Gmail')),
                ('my_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.about', verbose_name='My Name')),
            ],
        ),
    ]
