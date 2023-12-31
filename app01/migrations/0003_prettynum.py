# Generated by Django 4.2.4 on 2023-08-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_userinfo_creat_data_alter_userinfo_depart'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobil', models.CharField(max_length=11, verbose_name='手机号')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级'), (5, '5级')], default=1, verbose_name='级别')),
                ('statues', models.SmallIntegerField(default=2, verbose_name='状态')),
            ],
        ),
    ]
