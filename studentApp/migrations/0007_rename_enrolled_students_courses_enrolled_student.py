# Generated by Django 4.2.6 on 2023-10-05 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0006_remove_courses_enrolled_student_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='enrolled_students',
            new_name='enrolled_student',
        ),
    ]
