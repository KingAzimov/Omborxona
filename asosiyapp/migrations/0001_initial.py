# Generated by Django 4.1.1 on 2022-10-10 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('ism', models.CharField(max_length=50)),
                ('manzil', models.CharField(max_length=90)),
                ('tel', models.CharField(max_length=20)),
                ('qarz', models.PositiveSmallIntegerField(default=0)),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('narx', models.PositiveSmallIntegerField()),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('kelgan_sana', models.DateField()),
                ('olchov', models.CharField(max_length=30)),
                ('sotuvchi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.sotuvchi')),
            ],
        ),
    ]
