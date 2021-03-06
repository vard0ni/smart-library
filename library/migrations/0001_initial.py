# Generated by Django 2.2.13 on 2020-07-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True, verbose_name='Название книги')),
                ('author', models.CharField(max_length=120, null=True, verbose_name='Автор книги')),
                ('date_start', models.DateField(null=True, verbose_name='Дата взятия книги')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Дата возврата книги')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Просроченная дата возврата книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='ФИО')),
                ('education', models.CharField(max_length=50, verbose_name='Класс')),
                ('position', models.CharField(default='Ученик', max_length=100, verbose_name='Должность')),
                ('books', models.ManyToManyField(blank=True, to='library.Book')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
    ]
