# Generated by Django 5.0.7 on 2024-08-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2000-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]