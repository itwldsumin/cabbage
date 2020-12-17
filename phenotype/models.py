# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
#from django.conf import settings

class BaseModel(models.Model): 
    id = models.BigAutoField(primary_key=True)
    chrom = models.CharField(max_length=100)
    pos = models.IntegerField(blank=True, null=True)
    c_id = models.CharField(max_length=100, blank=True, null=True)
    ref_type = models.CharField(max_length=100, blank=True, null=True)
    alt_type = models.CharField(max_length=100, blank=True, null=True)
    qual = models.CharField(max_length=100, blank=True, null=True)#
    filtered = models.CharField(max_length=100, blank=True, null=True)#
    cabbage_id = models.IntegerField(db_column='cabbage_id')
    # brapa_id = models.CharField(max_length=100, blank=True, null=True)
    format = models.CharField(max_length=100, blank=True, null=True)
    snp_orign = models.CharField(max_length=100, blank=True, null=True)
    snp = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class AccessionsData(BaseModel):
    class Meta:
        managed = False
        db_table = 'accessions_data'
        ordering = ['-id']


class PhenotypeData(models.Model):
    #CabbageInfo=models.OneToOneField(settings.AUTH_CAB_MODEL, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    # brapa_id = models.CharField(max_length=100)
    cabbage_id = models.IntegerField(db_column='cabbage_id')
    ordernum = models.IntegerField(db_column='orderNum')  # Field name made lowercase.
    plant_height = models.FloatField(blank=True, null=True)
    plant_weigth = models.FloatField(blank=True, null=True)
    leaves = models.FloatField(blank=True, null=True)
    leaf_length = models.FloatField(blank=True, null=True)
    leaf_width = models.FloatField(blank=True, null=True)
    petiole_length = models.FloatField(blank=True, null=True)
    petiole_width = models.FloatField(blank=True, null=True)
    petiole_thickness = models.FloatField(blank=True, null=True)
    petiole_color = models.CharField(max_length=100, blank=True, null=True)
    petiole_section = models.CharField(max_length=100, blank=True, null=True)
    petiole_vessel_color = models.CharField(max_length=100, blank=True, null=True)
    head_weight = models.FloatField(blank=True, null=True)
    heading_habit = models.CharField(max_length=100, blank=True, null=True)
    head_shape = models.CharField(max_length=100, blank=True, null=True)
    head_forming_leaf_overlap = models.CharField(max_length=100, blank=True, null=True)
    color_outer_head_leaves = models.CharField(max_length=100, blank=True, null=True)
    head_solidity = models.CharField(max_length=100, blank=True, null=True)
    head_length = models.FloatField(blank=True, null=True)
    head_diameter = models.FloatField(blank=True, null=True)
    head_diameter_length = models.FloatField(blank=True, null=True)
    head_inner_leaves = models.IntegerField(blank=True, null=True)
    stem_length = models.FloatField(blank=True, null=True)
    stem_width = models.FloatField(blank=True, null=True)
    head_color = models.CharField(max_length=100, blank=True, null=True)
    trichome = models.CharField(max_length=100, blank=True, null=True)
    flowering_time = models.CharField(max_length=100, blank=True, null=True)
    img_path  = models.CharField(max_length=200, blank=True, null=True)
    img_path_u  = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'phenotype_data'


class CabbageInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    brapa_id = models.CharField(max_length=100)
    classification = models.CharField(max_length=100, blank=True, null=True)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    method_classfication = models.CharField(max_length=100, blank=True, null=True)
    line_info= models.CharField(max_length=1000, blank=True, null=True)
    line_source= models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabbage_info'