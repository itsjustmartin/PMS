# Generated by Django 4.2.1 on 2023-06-05 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Compamy',
            new_name='Company',
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={},
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=25),
        ),
    ]