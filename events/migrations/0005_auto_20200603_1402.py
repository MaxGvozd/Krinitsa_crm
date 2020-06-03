# Generated by Django 3.0.6 on 2020-06-03 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20200602_2342'),
        ('events', '0004_auto_20200602_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='contract',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='due_date',
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='goods.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sale',
            name='number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
