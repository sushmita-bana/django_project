# Generated by Django 4.1.4 on 2022-12-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_joining_people_aadharno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joining_people',
            name='AadharNo',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='joining_people',
            name='CourseFee',
            field=models.IntegerField(default=10),
        ),
    ]