# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Consent.q2'
        db.add_column('dm1_consent', 'q2', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'Consent.q3'
        db.add_column('dm1_consent', 'q3', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'Consent.q4'
        db.add_column('dm1_consent', 'q4', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'Consent.q5'
        db.add_column('dm1_consent', 'q5', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'Consent.q6'
        db.add_column('dm1_consent', 'q6', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Adding field 'Consent.q7'
        db.add_column('dm1_consent', 'q7', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True), keep_default=False)

        # Changing field 'Consent.q1'
        db.alter_column('dm1_consent', 'q1', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.consentdate'
        db.alter_column('dm1_consent', 'consentdate', self.gf('django.db.models.fields.DateField')(null=True))


    def backwards(self, orm):
        
        # Deleting field 'Consent.q2'
        db.delete_column('dm1_consent', 'q2')

        # Deleting field 'Consent.q3'
        db.delete_column('dm1_consent', 'q3')

        # Deleting field 'Consent.q4'
        db.delete_column('dm1_consent', 'q4')

        # Deleting field 'Consent.q5'
        db.delete_column('dm1_consent', 'q5')

        # Deleting field 'Consent.q6'
        db.delete_column('dm1_consent', 'q6')

        # Deleting field 'Consent.q7'
        db.delete_column('dm1_consent', 'q7')

        # Changing field 'Consent.q1'
        db.alter_column('dm1_consent', 'q1', self.gf('django.db.models.fields.CharField')(default='N', max_length=1))

        # Changing field 'Consent.consentdate'
        db.alter_column('dm1_consent', 'consentdate', self.gf('django.db.models.fields.DateField')(default='2'))


    models = {
        'dm1.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dm1.consent': {
            'Meta': {'object_name': 'Consent'},
            'consentdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'consentdateparentguardian': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'doctor_0': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctoraddress_0': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'doctortelephone_0': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'firstnameparentguardian': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'lastnameparentguardian': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'q1': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q2': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q3': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q4': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q5': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q6': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'q7': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'specialist_0': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        'dm1.diagnosis': {
            'Meta': {'ordering': "['patient']", 'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'diagnosed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'DM1'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['patients.Patient']", 'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'dm1.diagnosticcategory': {
            'Meta': {'object_name': 'DiagnosticCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'molecular_data': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['genetic.MolecularData']", 'unique': 'True', 'primary_key': 'True'}),
            'relative_cctg_repeat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relative_ctg_repeat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relative_test': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'repeat_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1.ethnicorigin': {
            'Meta': {'object_name': 'EthnicOrigin'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'dm1.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry_patient': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'dm1_familymember_related'", 'unique': 'True', 'null': 'True', 'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'dm1.fatigue': {
            'Meta': {'object_name': 'Fatigue'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'dm1.fatiguemedication': {
            'Meta': {'object_name': 'FatigueMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1.feedingfunction': {
            'Meta': {'object_name': 'FeedingFunction'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysphagia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'gastric_nasal_tube': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'dm1.generalmedicalfactors': {
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
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'endocrine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gall_bladder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geneticcounseling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'gor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medicalert': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'miscarriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obgyn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupationaltherapy': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'physiotherapy': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'pneumonia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'pneumoniaage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pneumoniainfections': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'psychological': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'psychologicalcounseling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'sexual_dysfunction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speechtherapy': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'vocationaltraining': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm1.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'dm1.heartmedication': {
            'Meta': {'object_name': 'HeartMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'acquisition_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'best_function': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {}),
            'sit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'walk_assisted_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'dm1.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'early_weakness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'face': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'flexor_digitorum_profundis': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'iliopsoas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'myotonia_effect': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'neck_flexion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'tibialis_anterior': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'})
        },
        'dm1.musclemedication': {
            'Meta': {'object_name': 'MuscleMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1.notes': {
            'Meta': {'object_name': 'Notes'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dm1.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dm1.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'age_non_invasive_ventilation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'dm1.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'dm1.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cardiac_implant_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'cataract_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract_diagnosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'})
        },
        'genetic.moleculardata': {
            'Meta': {'ordering': "['patient']", 'object_name': 'MolecularData'},
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['patients.Patient']", 'unique': 'True', 'primary_key': 'True'})
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

    complete_apps = ['dm1']
