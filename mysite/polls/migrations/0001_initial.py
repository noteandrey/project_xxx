# Generated by Django 3.2.4 on 2021-06-07 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TankAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, unique=True)),
                ('allocation', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='polls.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientRatio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=4, unique=True)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.drink')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='ingredient',
            field=models.ManyToManyField(through='polls.IngredientRatio', to='polls.Ingredient'),
        ),
    ]
