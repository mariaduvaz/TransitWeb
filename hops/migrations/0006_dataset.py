# Generated by Django 2.0.1 on 2018-05-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hops', '0005_auto_20180520_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frames', models.ManyToManyField(to='hops.Frame')),
            ],
        ),
    ]
