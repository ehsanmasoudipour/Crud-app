# Generated by Django 4.2.3 on 2023-07-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Automatic insertion of recordtime in database.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Automatic modification of recordtime in database.', verbose_name='modified')),
                ('description', models.TextField(help_text='Long Description.', verbose_name='Description')),
                ('title', models.CharField(help_text='title for tasks', max_length=100, unique=True, verbose_name='title')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
