# Generated by Django 2.1.1 on 2018-10-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bimestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('sequencia', models.IntegerField()),
                ('temnota', models.BooleanField()),
            ],
            options={
                'db_table': 'bimestre',
                'managed': False,
            },
        ),
    ]
