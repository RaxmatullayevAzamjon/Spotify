# Generated by Django 4.2.6 on 2023-10-25 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('sana', models.DateField()),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tugilgan_yil', models.CharField(max_length=30)),
                ('davlat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('janr', models.CharField(max_length=30)),
                ('davomiylik', models.TimeField(blank=True, null=True)),
                ('fayl', models.FileField(blank=True, null=True, upload_to='')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.qoshiqchi'),
        ),
    ]