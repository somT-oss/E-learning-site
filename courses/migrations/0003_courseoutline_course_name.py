# Generated by Django 3.1 on 2020-09-15 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200915_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoutline',
            name='course_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]