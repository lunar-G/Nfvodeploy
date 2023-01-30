# Generated by Django 4.1.5 on 2023-01-15 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_flowdetail_hard_timeout_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=256)),
                ('node_id', models.CharField(max_length=256)),
                ('table_id', models.CharField(max_length=256)),
                ('flow_id', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=256)),
                ('priority', models.CharField(max_length=256)),
                ('hard_timeout', models.CharField(max_length=256)),
                ('idle_timeout', models.CharField(max_length=256)),
                ('in_port', models.CharField(max_length=256)),
                ('output_port', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='FlowDetail',
        ),
    ]
