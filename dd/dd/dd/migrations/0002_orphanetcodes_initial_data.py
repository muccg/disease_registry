# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        from django.core.management import call_command
        call_command("loaddata", "dd.OrphanetChoices.json", exceptiononerror=True)


    def backwards(self, orm):
        "Write your backwards methods here."

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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orphanet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.OrphanetChoices']", 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
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
    symmetrical = True
