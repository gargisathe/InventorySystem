# Generated by Django 4.0 on 2022-06-28 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('uid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('father', models.CharField(max_length=30)),
                ('mother', models.CharField(max_length=30)),
                ('arrivalDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='PatientsRation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eoapp.patients')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
