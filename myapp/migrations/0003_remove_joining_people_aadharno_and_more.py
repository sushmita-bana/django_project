# Generated by Django 4.1.4 on 2022-12-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_joining_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joining_people',
            name='AadharNo',
        ),
        migrations.RemoveField(
            model_name='joining_people',
            name='CourseFee',
        ),
    ]
