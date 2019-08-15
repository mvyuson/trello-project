# Generated by Django 2.0.13 on 2019-08-15 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trello', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=200)),
                ('card_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello.Card')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='list_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello.List'),
        ),
    ]
