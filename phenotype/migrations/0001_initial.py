# Generated by Django 3.1.4 on 2020-12-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessionsData',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('chrom', models.CharField(max_length=100)),
                ('pos', models.IntegerField(blank=True, null=True)),
                ('c_id', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_type', models.CharField(blank=True, max_length=100, null=True)),
                ('alt_type', models.CharField(blank=True, max_length=100, null=True)),
                ('qual', models.CharField(blank=True, max_length=100, null=True)),
                ('filtered', models.CharField(blank=True, max_length=100, null=True)),
                ('cabbage_id', models.IntegerField(db_column='cabbage_id')),
                ('format', models.CharField(blank=True, max_length=100, null=True)),
                ('snp_orign', models.CharField(blank=True, max_length=100, null=True)),
                ('snp', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'accessions_data',
                'ordering': ['-id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PhenotypeData',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cabbage_id', models.IntegerField(db_column='cabbage_id')),
                ('ordernum', models.IntegerField(db_column='orderNum')),
                ('plant_height', models.FloatField(blank=True, null=True)),
                ('plant_weigth', models.FloatField(blank=True, null=True)),
                ('leaves', models.FloatField(blank=True, null=True)),
                ('leaf_length', models.FloatField(blank=True, null=True)),
                ('leaf_width', models.FloatField(blank=True, null=True)),
                ('petiole_length', models.FloatField(blank=True, null=True)),
                ('petiole_width', models.FloatField(blank=True, null=True)),
                ('petiole_thickness', models.FloatField(blank=True, null=True)),
                ('petiole_color', models.CharField(blank=True, max_length=100, null=True)),
                ('petiole_section', models.CharField(blank=True, max_length=100, null=True)),
                ('petiole_vessel_color', models.CharField(blank=True, max_length=100, null=True)),
                ('head_weight', models.FloatField(blank=True, null=True)),
                ('heading_habit', models.CharField(blank=True, max_length=100, null=True)),
                ('head_shape', models.CharField(blank=True, max_length=100, null=True)),
                ('head_forming_leaf_overlap', models.CharField(blank=True, max_length=100, null=True)),
                ('color_outer_head_leaves', models.CharField(blank=True, max_length=100, null=True)),
                ('head_solidity', models.CharField(blank=True, max_length=100, null=True)),
                ('head_length', models.FloatField(blank=True, null=True)),
                ('head_diameter', models.FloatField(blank=True, null=True)),
                ('head_diameter_length', models.FloatField(blank=True, null=True)),
                ('head_inner_leaves', models.IntegerField(blank=True, null=True)),
                ('stem_length', models.FloatField(blank=True, null=True)),
                ('stem_width', models.FloatField(blank=True, null=True)),
                ('head_color', models.CharField(blank=True, max_length=100, null=True)),
                ('trichome', models.CharField(blank=True, max_length=100, null=True)),
                ('flowering_time', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'phenotype_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CabbageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brapa_id', models.CharField(blank=True, max_length=100, null=True)),
                ('dassification', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
