import traceback
from django.db import models
from django.db.models.signals import post_save
from registry.patients.models import Patient

import logging
logger = logging.getLogger('genetic')

class Gene(models.Model):
    symbol = models.TextField()
    hgnc_id = models.TextField(verbose_name="HGNC ID")
    name = models.TextField()
    status = models.TextField()
    chromosome = models.TextField()
    accession_numbers = models.TextField()
    refseq_id = models.TextField(verbose_name="RefSeq ID")

    class Meta:
        ordering = ["symbol"]

    def __unicode__(self):
        return "%s (%s)" % (self.symbol, self.name)


class MolecularData(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)

    class Meta:
        ordering = ["patient"]
        verbose_name_plural = "molecular data"

    def __unicode__(self):
        return str(self.patient)

class MolecularDataSma(models.Model):
    patient = models.OneToOneField(Patient, primary_key=True)

    class Meta:
        ordering = ["patient"]
        verbose_name_plural = "molecular data"

    def __unicode__(self):
        return str(self.patient)

class Variation(models.Model):
    molecular_data = models.ForeignKey(MolecularData)
    gene = models.ForeignKey(Gene)
    exon = models.TextField(blank=True)
    exon_validation_override = models.BooleanField(default=False)
    dna_variation = models.TextField(verbose_name="DNA variation", help_text="Variation in standard HGVS sequence variation nomenclature", blank=True)
    dna_variation_validation_override = models.BooleanField(default=False)
    rna_variation = models.TextField(verbose_name="RNA variation", help_text="Variation in standard HGVS sequence variation nomenclature", blank=True)
    rna_variation_validation_override = models.BooleanField(default=False)
    protein_variation = models.TextField(verbose_name="protein variation", help_text="Variation in standard HGVS sequence variation nomenclature", blank=True)
    protein_variation_validation_override = models.BooleanField(default=False)
    technique = models.TextField()
    deletion_all_exons_tested = models.NullBooleanField(default=True, verbose_name="All Exons Tested (Deletions)")
    duplication_all_exons_tested = models.NullBooleanField(default=True, verbose_name="All Exons Tested (Duplications)")
    exon_boundaries_known = models.NullBooleanField(default=True, verbose_name="Exon Boundaries Known")
    point_mutation_all_exons_sequenced = models.NullBooleanField(default=True, verbose_name="All Exons Sequenced (Point Mutations)")
    all_exons_in_male_relative = models.NullBooleanField(verbose_name="All Exons Tested In Male Relative")

    VALIDATION_FIELDS = {
        "exon": "exon_validation_override",
        "dna": "dna_variation_validation_override",
        "rna": "rna_variation_validation_override",
        "protein": "protein_variation_validation_override",
    }

    class Meta:
        permissions = (
            ("can_override_validation", "Can override variation validation"),
        )

    def __unicode__(self):
        return str(self.molecular_data)

    def get_validation_overrides(self):
        overrides = {}

        for type, field in self.VALIDATION_FIELDS.iteritems():
            overrides[type] = getattr(self, field)

        return overrides

    def set_validation_override(self, type):
        setattr(self, self.VALIDATION_FIELDS[type], True)

class VariationSma(models.Model):
    SMN1_CHOICES = (
        (1, 'Homozygous'),
        (2, 'Heterozygous'),
        (3, 'No')
    )
    
    molecular_data = models.ForeignKey(MolecularDataSma)
    gene = models.ForeignKey(Gene)
    technique = models.TextField()
    exon_7_smn1_deletion = models.IntegerField(choices=SMN1_CHOICES, verbose_name = "Deletion of Exon 7 SMN1 gene")
    exon_7_sequencing = models.BooleanField(verbose_name="Exon 7 Sequencing")
    dna_variation = models.CharField(max_length=200, verbose_name="DNA variation")

    def __unicode__(self):
        return str(self.molecular_data)
    
    class Meta:
        verbose_name = "Molecular Data"
        verbose_name_plural = "Molecular Data Records"

class Laboratory(models.Model):
    """
    Laboratory is a model for preset values of "laboratory site"
    fields.
    """
    name = models.CharField(max_length=256)
    address = models.TextField(max_length=200, blank=True)
    contact_name = models.CharField(max_length=200, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "laboratories"

    def __unicode__(self):
        val = self.name
#        contacts = filter(bool, [self.contact_name, self.contact_email, self.contact_phone])
#        if self.address:
#            val = "%s, %s" % (val, self.address)
#        if contacts:
#            val = "%s; Contact: %s" % (val, ", ".join(contacts))
        return val

def signal_patient_post_save(sender, **kwargs):
    logger.debug("patient post_save signal")

    try:
        patient = kwargs['instance']
        moleculardata, created = MolecularData.objects.get_or_create(patient=patient)
        logger.debug("Molecular data record %s" % ("created" if created else "already existed"))
    except Exception, e:
        logger.critical(e)
        logger.critical(traceback.format_exc())
        raise


# connect up django signals
post_save.connect(signal_patient_post_save, sender=Patient)
