# Generated by Django 3.2.3 on 2021-08-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=64)),
                ('barcode', models.CharField(max_length=64, null=True)),
                ('book_in_here', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'library_booklist',
            },
        ),
    ]