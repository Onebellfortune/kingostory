# Generated by Django 3.0.7 on 2020-06-06 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('weapon', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Monsterstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hp', models.IntegerField(default=1)),
                ('boss', models.BooleanField(default=False)),
                ('probability', models.FloatField()),
                ('create_date', models.DateTimeField()),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Itemlist')),
            ],
        ),
        migrations.CreateModel(
            name='Itemstatus',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.Itemlist')),
                ('price', models.IntegerField()),
                ('itemlevel', models.IntegerField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Userstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=1)),
                ('money', models.IntegerField(default=0)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Useritem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Itemlist')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Userstatus')),
            ],
            options={
                'unique_together': {('uid', 'itemid')},
            },
        ),
        migrations.CreateModel(
            name='User_catch_Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catch_date', models.DateField()),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Monsterstatus')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Userstatus')),
            ],
            options={
                'unique_together': {('uid', 'mid')},
            },
        ),
    ]
