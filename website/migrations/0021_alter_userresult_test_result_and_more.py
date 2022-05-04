# Generated by Django 4.0.4 on 2022-05-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_remove_userresult_unique_quiz_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresult',
            name='test_result',
            field=models.JSONField(null=True),
        ),
        migrations.AddConstraint(
            model_name='userresult',
            constraint=models.UniqueConstraint(fields=('test_result', 'user'), name='unique_quiz_user'),
        ),
    ]
