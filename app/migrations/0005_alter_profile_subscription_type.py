# Generated by Django 3.2 on 2021-06-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscription_type',
            field=models.CharField(choices=[('Free', 'FREE'), ('Month', 'MONTHLY'), ('Year', 'YEARLY')], default='FREE', max_length=100),
        ),
    ]