# Generated by Django 2.2.12 on 2020-07-06 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0020_VIEW_GROUNDWATER_WELL'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='gwwaterbudget',
            name='gw_budget_valid_time',
        ),
        migrations.AlterField(
            model_name='gwflow',
            name='gw_flow_time',
            field=models.ForeignKey(blank=True, help_text='Refers to the duration, instant or interval of the flow (actual time, not observation time). E.g. "yearly", "summer", "2009" or "2009-2011".', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.TemporalType', verbose_name='GWFlowTime'),
        ),
    ]
