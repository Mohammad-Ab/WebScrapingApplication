# Generated by Django 4.2.4 on 2023-08-17 16:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ticker', models.CharField(max_length=255, unique=True)),
                ('industry_type', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='EsgScore',
            fields=[
                ('rank', models.IntegerField()),
                ('total_industries', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('esg_score', models.IntegerField()),
                ('environment_pillar', models.IntegerField()),
                ('social_pillar', models.IntegerField()),
                ('governance_pillar', models.IntegerField()),
                ('corporation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.corporation')),
            ],
            options={
                'ordering': ['esg_score', 'rank'],
            },
        ),
    ]
