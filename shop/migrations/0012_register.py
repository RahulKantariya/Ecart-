# Generated by Django 3.0.5 on 2020-05-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
