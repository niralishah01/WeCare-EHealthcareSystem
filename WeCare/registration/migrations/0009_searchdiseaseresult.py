# Generated by Django 3.0.2 on 2021-03-05 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_searchsymptomrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchDiseaseResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchcount', models.IntegerField(default=0)),
                ('diseasename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Disease')),
            ],
        ),
    ]