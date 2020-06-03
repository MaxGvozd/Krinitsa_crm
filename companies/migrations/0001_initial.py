# Generated by Django 3.0.6 on 2020-06-02 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=28)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('upn', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=350, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='companies.Bank_account')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=30)),
                ('start', models.DateField(auto_now=True)),
                ('end', models.DateField(blank=True, null=True)),
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
                ('address', models.CharField(blank=True, max_length=350, null=True)),
                ('telephone', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Company')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Contact_person')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='companies.Contract'),
        ),
        migrations.AddField(
            model_name='bank_account',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='companies.Currency'),
        ),
    ]
