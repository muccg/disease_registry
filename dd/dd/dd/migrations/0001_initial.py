# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table('dd_patient', (
            ('patient_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['patients.Patient'], unique=True, primary_key=True)),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('dd', ['Patient'])

        # Adding model 'LongitudinalSet'
        db.create_table('dd_longitudinalset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dd', ['LongitudinalSet'])

        # Adding model 'OrphanetChoices'
        db.create_table('dd_orphanetchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('dd', ['OrphanetChoices'])

        # Adding model 'LongitudinalData'
        db.create_table('dd_longitudinaldata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('dd', ['LongitudinalData'])

        # Adding model 'MedicalHistory'
        db.create_table('dd_medicalhistory', (
            ('longitudinalset_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LongitudinalSet'], unique=True, primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dd', ['MedicalHistory'])

        # Adding model 'MedicalHistoryRecord'
        db.create_table('dd_medicalhistoryrecord', (
            ('longitudinaldata_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LongitudinalData'], unique=True, primary_key=True)),
            ('medical_history', self.gf('django.db.models.fields.related.ForeignKey')(related_name='longitudinal_series', to=orm['dd.MedicalHistory'])),
        ))
        db.send_create_signal('dd', ['MedicalHistoryRecord'])

        # Adding model 'LabData'
        db.create_table('dd_labdata', (
            ('longitudinalset_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LongitudinalSet'], unique=True, primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dd', ['LabData'])

        # Adding model 'LabDataRecord'
        db.create_table('dd_labdatarecord', (
            ('longitudinaldata_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LongitudinalData'], unique=True, primary_key=True)),
            ('labdata_history', self.gf('django.db.models.fields.related.ForeignKey')(related_name='longitudinal_series', to=orm['dd.LabData'])),
        ))
        db.send_create_signal('dd', ['LabDataRecord'])

        # Adding model 'MRIData'
        db.create_table('dd_mridata', (
            ('longitudinalset_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LongitudinalSet'], unique=True, primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dd', ['MRIData'])

        # Adding model 'MRIDataRecord'
        db.create_table('dd_mridatarecord', (
            ('longitudinaldata_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LongitudinalData'], unique=True, primary_key=True)),
            ('mri_history', self.gf('django.db.models.fields.related.ForeignKey')(related_name='logitudinal_series', to=orm['dd.MRIData'])),
        ))
        db.send_create_signal('dd', ['MRIDataRecord'])

        # Adding model 'TreatmentOverview'
        db.create_table('dd_treatmentoverview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dd', ['TreatmentOverview'])

        # Adding model 'Treatment'
        db.create_table('dd_treatment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dd', ['Treatment'])

        # Adding model 'TreatmentCourse'
        db.create_table('dd_treatmentcourse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('treatment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Treatment'])),
            ('overview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.TreatmentOverview'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('dose', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('dd', ['TreatmentCourse'])

        # Adding model 'DDDiagnosis'
        db.create_table('dd_dddiagnosis', (
            ('patient', self.gf('django.db.models.fields.related.OneToOneField')(related_name='patient_diagnosis', unique=True, primary_key=True, to=orm['dd.Patient'])),
            ('diagnosis', self.gf('django.db.models.fields.CharField')(default='UNK', max_length=3)),
            ('affected_status', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('first_suspected_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('age_at_clinical_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('age_at_molecular_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orphanet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.OrphanetChoices'], null=True, blank=True)),
        ))
        db.send_create_signal('dd', ['DDDiagnosis'])

        # Adding model 'DDMedicalHistoryRecord'
        db.create_table('dd_ddmedicalhistoryrecord', (
            ('medicalhistoryrecord_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.MedicalHistoryRecord'], unique=True, primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDDiagnosis'], null=True, blank=True)),
            ('diabetes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diabetes_insulin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diabetes_onset_age', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('rheumatoid_arthritis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('crohns_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ulcerative_colitis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('psoriasis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('myasthenia_gravis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('vitiligo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thyroid_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thyroid_hypothyroidism', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thyroid_hashimotos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('graves_disease', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sjogrens_syndrome', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pernicious_anemia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('systemic_lupus_erythematosus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alopecia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('family_history_of_ms', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('dd', ['DDMedicalHistoryRecord'])

        # Adding model 'DDClinicalData'
        db.create_table('dd_ddclinicaldata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDDiagnosis'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('date_first_symtoms', self.gf('django.db.models.fields.DateField')()),
            ('edss_rating', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('past_medical_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDMedicalHistoryRecord'], null=True, blank=True)),
            ('date_of_visits', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('dd', ['DDClinicalData'])

        # Adding model 'DDLabDataRecord'
        db.create_table('dd_ddlabdatarecord', (
            ('labdatarecord_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LabDataRecord'], unique=True, primary_key=True)),
            ('protein', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('leucocytes', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('erythrocytes', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('oligoclonal_bands', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('igg_alb', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('dd', ['DDLabDataRecord'])

        # Adding model 'DDMRIDataRecord'
        db.create_table('dd_ddmridatarecord', (
            ('mridatarecord_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.MRIDataRecord'], unique=True, primary_key=True)),
            ('cds_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brain', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('spinal_cord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cervical', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thoracic', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dd', ['DDMRIDataRecord'])

        # Adding model 'DDMRIData'
        db.create_table('dd_ddmridata', (
            ('mridata_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.MRIData'], unique=True, primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDDiagnosis'], null=True, blank=True)),
        ))
        db.send_create_signal('dd', ['DDMRIData'])

        # Adding model 'DDLabData'
        db.create_table('dd_ddlabdata', (
            ('labdata_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.LabData'], unique=True, primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDDiagnosis'], null=True, blank=True)),
        ))
        db.send_create_signal('dd', ['DDLabData'])

        # Adding model 'DDTreatmentOverview'
        db.create_table('dd_ddtreatmentoverview', (
            ('treatmentoverview_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.TreatmentOverview'], unique=True, primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDDiagnosis'], null=True, blank=True)),
        ))
        db.send_create_signal('dd', ['DDTreatmentOverview'])

        # Adding M2M table for field treatments on 'DDTreatmentOverview'
        db.create_table('dd_ddtreatmentoverview_treatments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ddtreatmentoverview', models.ForeignKey(orm['dd.ddtreatmentoverview'], null=False)),
            ('treatment', models.ForeignKey(orm['dd.treatment'], null=False))
        ))
        db.create_unique('dd_ddtreatmentoverview_treatments', ['ddtreatmentoverview_id', 'treatment_id'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table('dd_patient')

        # Deleting model 'LongitudinalSet'
        db.delete_table('dd_longitudinalset')

        # Deleting model 'OrphanetChoices'
        db.delete_table('dd_orphanetchoices')

        # Deleting model 'LongitudinalData'
        db.delete_table('dd_longitudinaldata')

        # Deleting model 'MedicalHistory'
        db.delete_table('dd_medicalhistory')

        # Deleting model 'MedicalHistoryRecord'
        db.delete_table('dd_medicalhistoryrecord')

        # Deleting model 'LabData'
        db.delete_table('dd_labdata')

        # Deleting model 'LabDataRecord'
        db.delete_table('dd_labdatarecord')

        # Deleting model 'MRIData'
        db.delete_table('dd_mridata')

        # Deleting model 'MRIDataRecord'
        db.delete_table('dd_mridatarecord')

        # Deleting model 'TreatmentOverview'
        db.delete_table('dd_treatmentoverview')

        # Deleting model 'Treatment'
        db.delete_table('dd_treatment')

        # Deleting model 'TreatmentCourse'
        db.delete_table('dd_treatmentcourse')

        # Deleting model 'DDDiagnosis'
        db.delete_table('dd_dddiagnosis')

        # Deleting model 'DDMedicalHistoryRecord'
        db.delete_table('dd_ddmedicalhistoryrecord')

        # Deleting model 'DDClinicalData'
        db.delete_table('dd_ddclinicaldata')

        # Deleting model 'DDLabDataRecord'
        db.delete_table('dd_ddlabdatarecord')

        # Deleting model 'DDMRIDataRecord'
        db.delete_table('dd_ddmridatarecord')

        # Deleting model 'DDMRIData'
        db.delete_table('dd_ddmridata')

        # Deleting model 'DDLabData'
        db.delete_table('dd_ddlabdata')

        # Deleting model 'DDTreatmentOverview'
        db.delete_table('dd_ddtreatmentoverview')

        # Removing M2M table for field treatments on 'DDTreatmentOverview'
        db.delete_table('dd_ddtreatmentoverview_treatments')


    models = {
        'dd.ddclinicaldata': {
            'Meta': {'object_name': 'DDClinicalData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_first_symtoms': ('django.db.models.fields.DateField', [], {}),
            'date_of_visits': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDDiagnosis']"}),
            'edss_rating': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'past_medical_history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDMedicalHistoryRecord']", 'null': 'True', 'blank': 'True'})
        },
        'dd.dddiagnosis': {
            'Meta': {'object_name': 'DDDiagnosis'},
            'affected_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'UNK'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'orphanet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.OrphanetChoices']", 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['dd.Patient']"})
        },
        'dd.ddlabdata': {
            'Meta': {'object_name': 'DDLabData', '_ormbases': ['dd.LabData']},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDDiagnosis']", 'null': 'True', 'blank': 'True'}),
            'labdata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LabData']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dd.ddlabdatarecord': {
            'Meta': {'object_name': 'DDLabDataRecord', '_ormbases': ['dd.LabDataRecord']},
            'erythrocytes': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'igg_alb': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'labdatarecord_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LabDataRecord']", 'unique': 'True', 'primary_key': 'True'}),
            'leucocytes': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'oligoclonal_bands': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'protein': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        'dd.ddmedicalhistoryrecord': {
            'Meta': {'object_name': 'DDMedicalHistoryRecord', '_ormbases': ['dd.MedicalHistoryRecord']},
            'alopecia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'crohns_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes_insulin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes_onset_age': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDDiagnosis']", 'null': 'True', 'blank': 'True'}),
            'family_history_of_ms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graves_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medicalhistoryrecord_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.MedicalHistoryRecord']", 'unique': 'True', 'primary_key': 'True'}),
            'myasthenia_gravis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pernicious_anemia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'psoriasis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rheumatoid_arthritis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sjogrens_syndrome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'systemic_lupus_erythematosus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thyroid_disease': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thyroid_hashimotos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thyroid_hypothyroidism': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ulcerative_colitis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vitiligo': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dd.ddmridata': {
            'Meta': {'object_name': 'DDMRIData', '_ormbases': ['dd.MRIData']},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDDiagnosis']", 'null': 'True', 'blank': 'True'}),
            'mridata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.MRIData']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dd.ddmridatarecord': {
            'Meta': {'object_name': 'DDMRIDataRecord', '_ormbases': ['dd.MRIDataRecord']},
            'brain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cds_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cervical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mridatarecord_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.MRIDataRecord']", 'unique': 'True', 'primary_key': 'True'}),
            'spinal_cord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thoracic': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dd.ddtreatmentoverview': {
            'Meta': {'object_name': 'DDTreatmentOverview', '_ormbases': ['dd.TreatmentOverview']},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDDiagnosis']", 'null': 'True', 'blank': 'True'}),
            'treatmentoverview_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.TreatmentOverview']", 'unique': 'True', 'primary_key': 'True'}),
            'treatments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dd.Treatment']", 'null': 'True', 'blank': 'True'})
        },
        'dd.labdata': {
            'Meta': {'object_name': 'LabData', '_ormbases': ['dd.LongitudinalSet']},
            'longitudinalset_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LongitudinalSet']", 'unique': 'True', 'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
        },
        'dd.labdatarecord': {
            'Meta': {'object_name': 'LabDataRecord', '_ormbases': ['dd.LongitudinalData']},
            'labdata_history': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'longitudinal_series'", 'to': "orm['dd.LabData']"}),
            'longitudinaldata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LongitudinalData']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dd.longitudinaldata': {
            'Meta': {'object_name': 'LongitudinalData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dd.longitudinalset': {
            'Meta': {'object_name': 'LongitudinalSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dd.medicalhistory': {
            'Meta': {'object_name': 'MedicalHistory', '_ormbases': ['dd.LongitudinalSet']},
            'longitudinalset_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LongitudinalSet']", 'unique': 'True', 'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
        },
        'dd.medicalhistoryrecord': {
            'Meta': {'object_name': 'MedicalHistoryRecord', '_ormbases': ['dd.LongitudinalData']},
            'longitudinaldata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LongitudinalData']", 'unique': 'True', 'primary_key': 'True'}),
            'medical_history': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'longitudinal_series'", 'to': "orm['dd.MedicalHistory']"})
        },
        'dd.mridata': {
            'Meta': {'object_name': 'MRIData', '_ormbases': ['dd.LongitudinalSet']},
            'longitudinalset_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LongitudinalSet']", 'unique': 'True', 'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
        },
        'dd.mridatarecord': {
            'Meta': {'object_name': 'MRIDataRecord', '_ormbases': ['dd.LongitudinalData']},
            'longitudinaldata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.LongitudinalData']", 'unique': 'True', 'primary_key': 'True'}),
            'mri_history': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logitudinal_series'", 'to': "orm['dd.MRIData']"})
        },
        'dd.orphanetchoices': {
            'Meta': {'ordering': "['code']", 'object_name': 'OrphanetChoices'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dd.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'object_name': 'Patient', '_ormbases': ['patients.Patient']},
            'patient_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['patients.Patient']", 'unique': 'True', 'primary_key': 'True'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'dd.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dd.treatmentcourse': {
            'Meta': {'object_name': 'TreatmentCourse'},
            'dose': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'overview': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.TreatmentOverview']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Treatment']"})
        },
        'dd.treatmentoverview': {
            'Meta': {'object_name': 'TreatmentOverview'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
        },
        'groups.workinggroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'WorkingGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'patients.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        'patients.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surgery_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'patients.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'unique_together': "(('family_name', 'given_names', 'working_group'),)", 'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Doctor']", 'through': "orm['patients.PatientDoctor']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_address': ('django.db.models.fields.TextField', [], {}),
            'next_of_kin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_of_kin_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_of_kin_home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_postcode': ('django.db.models.fields.IntegerField', [], {}),
            'next_of_kin_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'next_of_kin_set'", 'to': "orm['patients.State']"}),
            'next_of_kin_suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'next_of_kin_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.WorkingGroup']"})
        },
        'patients.patientdoctor': {
            'Meta': {'object_name': 'PatientDoctor'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Doctor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dd']