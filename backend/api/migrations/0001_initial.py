# Generated by Django 4.2.4 on 2023-09-15 15:57

from django.db import migrations, models


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
                ('rank', models.IntegerField()),
                ('total_industries', models.IntegerField()),
                ('esg_score', models.IntegerField()),
                ('environment_pillar', models.IntegerField()),
                ('social_pillar', models.IntegerField()),
                ('governance_pillar', models.IntegerField()),
            ],
            options={
                'ordering': ['title', 'esg_score', 'rank'],
            },
        ),
    ]
