# Generated by Django 3.2 on 2021-06-15 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('course_name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_premium', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_module_name', models.CharField(max_length=250)),
                ('course_description', models.TextField()),
                ('video_url', models.URLField(max_length=300)),
                ('can_view', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
    ]
