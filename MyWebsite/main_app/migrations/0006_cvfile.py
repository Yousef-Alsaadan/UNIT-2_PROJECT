# Generated by Django 4.2.1 on 2023-06-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_file', models.FileField(default='pdf/Yousef_Mohammed_Resume.pdf', upload_to='pdf/')),
            ],
        ),
    ]
