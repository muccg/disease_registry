# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ClinicalTrials.id'
        db.add_column('dm1_questionnaire_clinicaltrials', 'id',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ClinicalTrials.id'
        db.delete_column('dm1_questionnaire_clinicaltrials', 'id')


    models = {
        'dm1.cancertypechoices': {
            'Meta': {'ordering': "['description']", 'object_name': 'CancerTypeChoices'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dm1_questionnaire.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.consent': {
            'Meta': {'object_name': 'Consent'},
            'consentdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'consentdateparentguardian': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'doctor_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctor_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'firstnameparentguardian': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'lastnameparentguardian': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'q1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q6': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q7': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'specialist_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'specialist_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Patient']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dm1_questionnaire.ethnicorigin': {
            'Meta': {'object_name': 'EthnicOrigin'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']"}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.fatigue': {
            'Meta': {'object_name': 'Fatigue'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fatigue': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'in_car': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lying_down_afternoon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'passenger_car': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_inactive_public': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_quietly_lunch': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_reading': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_talking': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'watching_tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.fatiguemedication': {
            'Meta': {'object_name': 'FatigueMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.feedingfunction': {
            'Meta': {'object_name': 'FeedingFunction'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysphagia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'gastric_nasal_tube': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.generalmedicalfactors': {
            'Meta': {'object_name': 'GeneralMedicalFactors'},
            'anxiety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apathy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cancer': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'cancerorgan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancerothers': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancertype': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dm1questcancertypechoices'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['dm1.CancerTypeChoices']"}),
            'cholesterol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognitive_impairment': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'constipation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'diabetesage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'dm1_quest.diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['dm1_questionnaire.Diagnosis']"}),
            'endocrine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gall_bladder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medicalert': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'miscarriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obgyn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupationaltherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'physiotherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'pneumonia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'pneumoniaage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pneumoniainfections': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'psychological': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'psychologicalcounseling': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'sexual_dysfunction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speechtherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'vocationaltraining': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ecg': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'ecg_examination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_pr_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_qrs_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_sinus_rhythm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'echocardiogram': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'echocardiogram_lvef': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'echocardiogram_lvef_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fainting': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'palpitations': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'racing': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.heartmedication': {
            'Meta': {'object_name': 'HeartMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'best_function': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'walk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'walk_assisted_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12'})
        },
        'dm1_questionnaire.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.musclemedication': {
            'Meta': {'object_name': 'MuscleMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'object_name': 'Patient'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dm1_questionnaire_patient_set'", 'to': "orm['patients.Country']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dm1_questionnaire_patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dm1_questionnaire_patient_set'", 'to': "orm['groups.WorkingGroup']"})
        },
        'dm1_questionnaire.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'age_non_invasive_ventilation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calculatedfvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cardiac_implant_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'cataract_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract_diagnosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'})
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
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dm1_questionnaire']