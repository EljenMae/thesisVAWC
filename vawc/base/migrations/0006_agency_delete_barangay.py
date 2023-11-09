# Generated by Django 4.2.4 on 2023-11-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_agencies_barangay_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyName', models.CharField(max_length=200)),
                ('agencyAddress', models.CharField(blank=True, max_length=200)),
                ('contactPerson', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('contactNum', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Barangay',
        ),
    ]