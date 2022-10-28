# Generated by Django 4.1.2 on 2022-10-27 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('busImage', models.ImageField(null=True, upload_to='buses')),
                ('shiftsTo', models.IntegerField()),
                ('shiftsFrom', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('busCompany', models.CharField(max_length=30)),
                ('setOffTime', models.CharField(max_length=30)),
                ('startLocation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transportug.buscompany')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberPlate', models.CharField(max_length=30)),
                ('mainOffices', models.CharField(max_length=30)),
                ('travelTime', models.TimeField()),
                ('seats', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportug.buscompany')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='regions', to='transportug.buscompany')),
            ],
        ),
    ]
