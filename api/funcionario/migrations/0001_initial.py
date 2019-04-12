# Generated by Django 2.1.5 on 2019-01-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviacao', models.CharField(max_length=255, null=True, verbose_name='abreviacacao')),
                ('descricao', models.CharField(max_length=255, null=True, verbose_name='descricao')),
            ],
            options={
                'db_table': 'cargo',
                'ordering': ('id',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolaridade', models.CharField(max_length=255, null=True, verbose_name='escolaridade')),
                ('cargahoraria', models.CharField(max_length=255, null=True, verbose_name='cargahoraria')),
                ('situacaofuncional', models.CharField(max_length=255, null=True, verbose_name='situacaofuncional')),
                ('dataadmissao', models.DateField(verbose_name='dataadmissao')),
                ('statusfuncionario', models.CharField(max_length=255, null=True, verbose_name='statusfuncionario')),
            ],
            options={
                'db_table': 'funcionario',
                'ordering': ('id',),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FuncionarioEscola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(verbose_name='ativo')),
            ],
            options={
                'db_table': 'funcionarioescola',
                'ordering': ('id',),
                'managed': False,
            },
        ),
    ]
