# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Muscle.myotonia_effect'
        db.add_column('dm1_questionnaire_muscle', 'myotonia_effect', self.gf('django.db.models.fields.CharField')(default='N', max_length=6), keep_default=False)

        # Adding field 'GeneralMedicalFactors.medicalert'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'medicalert', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneralMedicalFactors.physiotherapy'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'physiotherapy', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneralMedicalFactors.geneticcounseling'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'geneticcounseling', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneralMedicalFactors.psychologicalcounseling'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'psychologicalcounseling', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneralMedicalFactors.speechtherapy'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'speechtherapy', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneralMedicalFactors.occupationaltherapy'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'occupationaltherapy', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneralMedicalFactors.vocationaltraining'
        db.add_column('dm1_questionnaire_generalmedicalfactors', 'vocationaltraining', self.gf('django.db.models.fields.CharField')(default='0', max_length=1), keep_default=False)

        # Adding field 'GeneticTestDetails.counselling'
        db.add_column('dm1_questionnaire_genetictestdetails', 'counselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'GeneticTestDetails.familycounselling'
        db.add_column('dm1_questionnaire_genetictestdetails', 'familycounselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'Heart.racing'
        db.add_column('dm1_questionnaire_heart', 'racing', self.gf('django.db.models.fields.CharField')(default='N', max_length=1), keep_default=False)

        # Adding field 'Heart.palpitations'
        db.add_column('dm1_questionnaire_heart', 'palpitations', self.gf('django.db.models.fields.CharField')(default='N', max_length=1), keep_default=False)

        # Adding field 'Heart.fainting'
        db.add_column('dm1_questionnaire_heart', 'fainting', self.gf('django.db.models.fields.CharField')(default='2', max_length=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Muscle.myotonia_effect'
        db.delete_column('dm1_questionnaire_muscle', 'myotonia_effect')

        # Deleting field 'GeneralMedicalFactors.medicalert'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'medicalert')

        # Deleting field 'GeneralMedicalFactors.physiotherapy'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'physiotherapy')

        # Deleting field 'GeneralMedicalFactors.geneticcounseling'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'geneticcounseling')

        # Deleting field 'GeneralMedicalFactors.psychologicalcounseling'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'psychologicalcounseling')

        # Deleting field 'GeneralMedicalFactors.speechtherapy'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'speechtherapy')

        # Deleting field 'GeneralMedicalFactors.occupationaltherapy'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'occupationaltherapy')

        # Deleting field 'GeneralMedicalFactors.vocationaltraining'
        db.delete_column('dm1_questionnaire_generalmedicalfactors', 'vocationaltraining')

        # Deleting field 'GeneticTestDetails.counselling'
        db.delete_column('dm1_questionnaire_genetictestdetails', 'counselling')

        # Deleting field 'GeneticTestDetails.familycounselling'
        db.delete_column('dm1_questionnaire_genetictestdetails', 'familycounselling')

        # Deleting field 'Heart.racing'
        db.delete_column('dm1_questionnaire_heart', 'racing')

        # Deleting field 'Heart.palpitations'
        db.delete_column('dm1_questionnaire_heart', 'palpitations')

        # Deleting field 'Heart.fainting'
        db.delete_column('dm1_questionnaire_heart', 'fainting')


    models = {
        'dm1_questionnaire.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dm1_questionnaire.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Patient']", 'unique': 'True', 'primary_key': 'True'}),
            'undiagnosed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dm1_questionnaire.ethnicorigin': {
            'Meta': {'object_name': 'EthnicOrigin'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.fatigue': {
            'Meta': {'object_name': 'Fatigue'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fatigue': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
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
            'cancer': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'cancerorgan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancerothers': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancertype': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cholesterol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognitive_impairment': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'constipation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'diabetesage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'endocrine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gall_bladder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geneticcounseling': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medicalert': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'miscarriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obgyn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupationaltherapy': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'physiotherapy': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'pneumonia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'pneumoniaage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pneumoniainfections': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'psychological': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'psychologicalcounseling': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'sexual_dysfunction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speechtherapy': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'vocationaltraining': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm1_questionnaire.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ecg': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'ecg_examination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_pr_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_qrs_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_sinus_rhythm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'echocardiogram': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'echocardiogram_lvef': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'echocardiogram_lvef_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fainting': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'palpitations': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'racing': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'dm1_questionnaire.heartmedication': {
            'Meta': {'object_name': 'HeartMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'acquisition_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'best_function': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {}),
            'sit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'walk_assisted_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'dm1_questionnaire.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'myotonia_effect': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'dm1_questionnaire.musclemedication': {
            'Meta': {'object_name': 'MuscleMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
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
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'dm1_questionnaire.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
