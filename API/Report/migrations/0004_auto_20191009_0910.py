# Generated by Django 2.2.5 on 2019-10-09 09:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0003_auto_20191008_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancedatamodel',
            name='source',
            field=models.IntegerField(choices=[(0, '新增成交'), (2, '公海成交'), (1, '回访成交')], default=0, verbose_name='数据来源'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='status',
            field=models.IntegerField(choices=[(0, '老员工'), (1, '新员工'), (2, '离职')], default=0, verbose_name='员工状态'),
        ),
        migrations.CreateModel(
            name='TransferPerformanceDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('development_volume', models.IntegerField(blank=True, default=0, null=True, verbose_name='开发量')),
                ('transfer_volume', models.IntegerField(blank=True, default=0, null=True, verbose_name='转接量')),
                ('data_time', models.DateField(default=django.utils.timezone.now, verbose_name='数据日期')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Report.PersonModel', verbose_name='成员ID')),
            ],
            options={
                'verbose_name': '转接绩效数据表',
                'verbose_name_plural': '转接绩效数据表',
                'db_table': 'Report_Transfer_PerformanceData',
                'ordering': ['-id', '-data_time', '-date_joined'],
            },
        ),
    ]
