# Generated by Django 2.1.2 on 2018-11-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0005_auto_20181119_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerieTurma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'serieturma',
                'ordering': ('id',),
                'managed': False,
            },
        ),
    ]
