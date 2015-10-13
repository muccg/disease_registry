# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Diagnosis.diagnosis'
        db.alter_column(u'dd_diagnosis', 'diagnosis_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DiagnosedCondition'], null=True, on_delete=models.SET_NULL))
        # Adding field 'LabData.vitamin_d3'
        db.add_column(u'dd_labdata', 'vitamin_d3',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'LabData.aqp4_antiody'
        db.add_column(u'dd_labdata', 'aqp4_antiody',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


        # Changing field 'LabData.oligoclonal_bands'
        db.alter_column(u'dd_labdata', 'oligoclonal_bands', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'LabData.leucocytes'
        db.alter_column(u'dd_labdata', 'leucocytes', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'LabData.erythrocytes'
        db.alter_column(u'dd_labdata', 'erythrocytes', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'LabData.igg_alb'
        db.alter_column(u'dd_labdata', 'igg_alb', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'LabData.protein'
        db.alter_column(u'dd_labdata', 'protein', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'Diagnosis.diagnosis'
        db.alter_column(u'dd_diagnosis', 'diagnosis_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DiagnosedCondition'], null=True))
        # Deleting field 'LabData.vitamin_d3'
        db.delete_column(u'dd_labdata', 'vitamin_d3')

        # Deleting field 'LabData.aqp4_antiody'
        db.delete_column(u'dd_labdata', 'aqp4_antiody')


        # Changing field 'LabData.oligoclonal_bands'
        db.alter_column(u'dd_labdata', 'oligoclonal_bands', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'LabData.leucocytes'
        db.alter_column(u'dd_labdata', 'leucocytes', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'LabData.erythrocytes'
        db.alter_column(u'dd_labdata', 'erythrocytes', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'LabData.igg_alb'
        db.alter_column(u'dd_labdata', 'igg_alb', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'LabData.protein'
        db.alter_column(u'dd_labdata', 'protein', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        u'dd.ddclinicaldata': {
            'Meta': {'object_name': 'DDClinicalData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_first_symtoms': ('django.db.models.fields.DateField', [], {}),
            'date_of_visits': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.Diagnosis']"}),
            'edss_ambulation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_bowel_bladder': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_brainstem': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_cerebellar': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_cerebral_mental': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_evaluation_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'edss_form': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'edss_pyramidal': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_sensory': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'edss_visual': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dd.diagnosedcondition': {
            'Meta': {'object_name': 'DiagnosedCondition'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dd.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'affected_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_diagnosis': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_first_symptom': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.DiagnosedCondition']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'family_consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_history': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'orphanet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.OrphanetChoices']", 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['patients.Patient']"}),
            'treatments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dd.Treatment']", 'through': u"orm['dd.TreatmentCourse']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'dd.labdata': {
            'Meta': {'object_name': 'LabData'},
            'aqp4_antiody': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.Diagnosis']"}),
            'erythrocytes': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igg_alb': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'leucocytes': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'oligoclonal_bands': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'protein': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vitamin_d3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'dd.medicalhistory': {
            'Meta': {'object_name': 'MedicalHistory'},
            'chronic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'medical_history'", 'to': u"orm['dd.Diagnosis']"}),
            'disease': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.MedicalHistoryDisease']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical_history_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'misdiagnosed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'dd.medicalhistorydisease': {
            'Meta': {'ordering': "['disease']", 'object_name': 'MedicalHistoryDisease'},
            'disease': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dd.mridata': {
            'Meta': {'object_name': 'MRIData'},
            'brain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cervical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.Diagnosis']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'report_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'thoracic': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'dd.mrifile': {
            'Meta': {'object_name': 'MRIFile'},
            'data': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['dd.MRIData']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'dd.orphanetchoices': {
            'Meta': {'ordering': "['code']", 'object_name': 'OrphanetChoices'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dd.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dd.treatmentcourse': {
            'Meta': {'object_name': 'TreatmentCourse'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.Diagnosis']"}),
            'dose_other': ('django.db.models.fields.TextField', [], {}),
            'dose_type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dd.Treatment']"})
        },
        u'groups.workinggroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'WorkingGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'patients.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'patients.doctor': {
            'Meta': {'ordering': "['family_name']", 'object_name': 'Doctor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surgery_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'patients.nextofkinrelationship': {
            'Meta': {'object_name': 'NextOfKinRelationship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patients.parent': {
            'Meta': {'object_name': 'Parent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_date_of_migration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'parent_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patients.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'unique_together': "(('family_name', 'given_names', 'working_group'),)", 'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'date_of_migration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patients.Doctor']", 'through': u"orm['patients.PatientDoctor']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactive_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'next_of_kin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_parent_place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_postcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'next_of_kin_relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.NextOfKinRelationship']", 'null': 'True', 'blank': 'True'}),
            'next_of_kin_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'next_of_kin_set'", 'null': 'True', 'to': u"orm['patients.State']"}),
            'next_of_kin_suburb': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patients.Parent']", 'through': u"orm['patients.PatientParent']", 'symmetrical': 'False'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_set'", 'to': u"orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'umrn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['groups.WorkingGroup']"})
        },
        u'patients.patientdoctor': {
            'Meta': {'object_name': 'PatientDoctor'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'patients.patientparent': {
            'Meta': {'object_name': 'PatientParent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Parent']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dd']