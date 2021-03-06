# Generated by Django 2.1.5 on 2019-01-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalEscola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='descricao')),
            ],
            options={
                'db_table': 'localescola',
                'ordering': ('id',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='descricao')),
                ('nivel', models.CharField(max_length=255, verbose_name='nivel')),
            ],
            options={
                'db_table': 'serie',
                'ordering': ('id',),
                'managed': False,
            },
        ),
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
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='descricao')),
                ('turno', models.CharField(max_length=255, verbose_name='turno')),
                ('nivel', models.CharField(max_length=255, verbose_name='nivel')),
                ('statusturma', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'turma',
                'ordering': ('id',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviacao', models.CharField(max_length=255, verbose_name='abreviacao')),
                ('cnpj', models.CharField(max_length=255, verbose_name='cnpj')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
            ],
            options={
                'db_table': 'unidade',
                'ordering': ('id',),
                'managed': False,
            },
        ),
    ]
