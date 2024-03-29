# Generated by Django 4.2.10 on 2024-03-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_subscription'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('student', 'course'), name='unique_student_course'),
        ),
    ]