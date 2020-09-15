# Generated by Django 2.0.1 on 2020-09-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]