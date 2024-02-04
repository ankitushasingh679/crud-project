# Generated by Django 4.2.3 on 2023-09-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysqlcrud1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('umail', models.EmailField(max_length=50)),
                ('upassword', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
