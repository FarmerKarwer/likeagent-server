# Generated by Django 4.0.4 on 2022-05-01 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='max_score',
        ),
        migrations.RemoveField(
            model_name='result',
            name='min_score',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='brief_description',
            field=models.TextField(max_length=350),
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1500)),
                ('min_score', models.IntegerField()),
                ('max_score', models.IntegerField()),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.result')),
            ],
        ),
    ]
