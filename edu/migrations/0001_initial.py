# Generated by Django 2.2.7 on 2019-11-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('course_number', models.CharField(max_length=200)),
                ('group_number', models.CharField(max_length=200)),
                ('teacher', models.CharField(max_length=200)),
                ('start_time', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
                ('first_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=200)),
                ('second_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=200)),
            ],
        ),
    ]
