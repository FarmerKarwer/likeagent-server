# Generated by Django 4.0.4 on 2022-05-03 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0011_alter_userresult_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userresult',
            unique_together={('user', 'quiz')},
        ),
    ]