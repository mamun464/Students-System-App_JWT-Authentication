# Generated by Django 4.2.6 on 2023-10-05 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0003_remove_students_course_enrolled_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name_plural': 'Students'},
        ),
    ]
