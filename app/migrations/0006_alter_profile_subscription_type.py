# Generated by Django 3.2 on 2021-06-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_profile_subscription_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscription_type',
            field=models.CharField(choices=[('F', 'FREE'), ('M', 'MONTHLY'), ('Y', 'YEARLY')], default='FREE', max_length=100),
        ),
    ]