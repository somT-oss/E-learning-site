# Generated by Django 3.1 on 2020-09-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_description',
        ),
        migrations.AddField(
            model_name='courseoutline',
            name='course_description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_datestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
