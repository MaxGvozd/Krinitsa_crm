# Generated by Django 3.0.6 on 2020-05-29 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0002_auto_20200529_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(blank=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('upn', models.PositiveIntegerField(unique=True)),
                ('address', models.CharField(max_length=350)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='companies.Bank_account')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('birthday', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=30)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(blank=True)),
                ('due_date_payment', models.PositiveSmallIntegerField(default=45)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=4)),
                ('capacity', models.PositiveSmallIntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=350)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Contact_person')),
                ('service_area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.Service_area')),
            ],
        ),
        migrations.AddField(
            model_name='bank_account',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Currency'),
        ),
    ]
