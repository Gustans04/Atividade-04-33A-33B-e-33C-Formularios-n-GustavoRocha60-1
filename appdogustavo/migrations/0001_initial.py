# Generated by Django 3.2.13 on 2023-09-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('relevancia', models.CharField(max_length=70)),
                ('prioridade', models.IntegerField()),
                ('categoria', models.CharField(choices=[('B', 'Bonito'), ('E', 'Engraçado'), ('C', 'Competitivo')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20)),
                ('tamanho', models.IntegerField()),
                ('peso', models.IntegerField()),
            ],
        ),
    ]
