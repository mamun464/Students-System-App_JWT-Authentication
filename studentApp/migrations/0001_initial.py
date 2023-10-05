# Generated by Django 4.2.6 on 2023-10-05 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('s_id', models.CharField(max_length=50, unique=True)),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('course_enrolled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentApp.courses')),
            ],
        ),
    ]
