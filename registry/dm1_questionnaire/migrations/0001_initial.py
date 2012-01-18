# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Patient'
        db.create_table('dm1_questionnaire_patient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('working_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dm1_questionnaire_patient_set', to=orm['groups.WorkingGroup'])),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('given_names', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dm1_questionnaire_patient_set', to=orm['patients.State'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dm1_questionnaire_patient_set', to=orm['patients.Country'])),
            ('postcode', self.gf('django.db.models.fields.IntegerField')()),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Patient'])

        # Adding model 'Diagnosis'
        db.create_table('dm1_questionnaire_diagnosis', (
            ('affectedstatus', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_symptom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_suspected_by', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('undiagnosed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('age_at_clinical_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('age_at_molecular_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Patient'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Diagnosis'])

        # Adding model 'MotorFunction'
        db.create_table('dm1_questionnaire_motorfunction', (
            ('walk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('walk_assisted', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('walk_assisted_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_function', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('acquisition_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('wheelchair_use', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('wheelchair_usage_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dysarthria', self.gf('django.db.models.fields.IntegerField')()),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['MotorFunction'])

        # Adding model 'Surgery'
        db.create_table('dm1_questionnaire_surgery', (
            ('cardiac_implant', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cardiac_implant_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cataract_diagnosis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cataract', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('cataract_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Surgery'])

        # Adding model 'Heart'
        db.create_table('dm1_questionnaire_heart', (
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('age_at_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ecg', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('ecg_sinus_rhythm', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('ecg_pr_interval', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ecg_qrs_duration', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ecg_examination_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('echocardiogram', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('echocardiogram_lvef', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('echocardiogram_lvef_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Heart'])

        # Adding model 'HeartMedication'
        db.create_table('dm1_questionnaire_heartmedication', (
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['HeartMedication'])

        # Adding model 'Respiratory'
        db.create_table('dm1_questionnaire_respiratory', (
            ('non_invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('age_non_invasive_ventilation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('non_invasive_ventilation_type', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fvc', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fvc_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Respiratory'])

        # Adding model 'Muscle'
        db.create_table('dm1_questionnaire_muscle', (
            ('myotonia', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Muscle'])

        # Adding model 'MuscleMedication'
        db.create_table('dm1_questionnaire_musclemedication', (
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['MuscleMedication'])

        # Adding model 'FeedingFunction'
        db.create_table('dm1_questionnaire_feedingfunction', (
            ('dysphagia', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('gastric_nasal_tube', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['FeedingFunction'])

        # Adding model 'Fatigue'
        db.create_table('dm1_questionnaire_fatigue', (
            ('fatigue', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('sitting_reading', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('watching_tv', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_inactive_public', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('passenger_car', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lying_down_afternoon', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_talking', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_quietly_lunch', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('in_car', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['Fatigue'])

        # Adding model 'FatigueMedication'
        db.create_table('dm1_questionnaire_fatiguemedication', (
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['FatigueMedication'])

        # Adding model 'SocioeconomicFactors'
        db.create_table('dm1_questionnaire_socioeconomicfactors', (
            ('education', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('employment_effect', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['SocioeconomicFactors'])

        # Adding model 'GeneralMedicalFactors'
        db.create_table('dm1_questionnaire_generalmedicalfactors', (
            ('diabetes', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('diabetesage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pneumonia', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('pneumoniaage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pneumoniainfections', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('cancer', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('cancertype', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('cancerothers', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('cancerorgan', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('liver', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('miscarriage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gall_bladder', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('infection', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sexual_dysfunction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('constipation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cholesterol', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cognitive_impairment', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('psychological', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anxiety', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('depression', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apathy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('endocrine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('obgyn', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['GeneralMedicalFactors'])

        # Adding model 'GeneticTestDetails'
        db.create_table('dm1_questionnaire_genetictestdetails', (
            ('details', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('test_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('laboratory', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['GeneticTestDetails'])

        # Adding model 'EthnicOrigin'
        db.create_table('dm1_questionnaire_ethnicorigin', (
            ('ethnic_origin', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['EthnicOrigin'])

        # Adding model 'ClinicalTrials'
        db.create_table('dm1_questionnaire_clinicaltrials', (
            ('drug_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_sponsor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_phase', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('dm1_questionnaire', ['ClinicalTrials'])


    def backwards(self, orm):
        
        # Deleting model 'Patient'
        db.delete_table('dm1_questionnaire_patient')

        # Deleting model 'Diagnosis'
        db.delete_table('dm1_questionnaire_diagnosis')

        # Deleting model 'MotorFunction'
        db.delete_table('dm1_questionnaire_motorfunction')

        # Deleting model 'Surgery'
        db.delete_table('dm1_questionnaire_surgery')

        # Deleting model 'Heart'
        db.delete_table('dm1_questionnaire_heart')

        # Deleting model 'HeartMedication'
        db.delete_table('dm1_questionnaire_heartmedication')

        # Deleting model 'Respiratory'
        db.delete_table('dm1_questionnaire_respiratory')

        # Deleting model 'Muscle'
        db.delete_table('dm1_questionnaire_muscle')

        # Deleting model 'MuscleMedication'
        db.delete_table('dm1_questionnaire_musclemedication')

        # Deleting model 'FeedingFunction'
        db.delete_table('dm1_questionnaire_feedingfunction')

        # Deleting model 'Fatigue'
        db.delete_table('dm1_questionnaire_fatigue')

        # Deleting model 'FatigueMedication'
        db.delete_table('dm1_questionnaire_fatiguemedication')

        # Deleting model 'SocioeconomicFactors'
        db.delete_table('dm1_questionnaire_socioeconomicfactors')

        # Deleting model 'GeneralMedicalFactors'
        db.delete_table('dm1_questionnaire_generalmedicalfactors')

        # Deleting model 'GeneticTestDetails'
        db.delete_table('dm1_questionnaire_genetictestdetails')

        # Deleting model 'EthnicOrigin'
        db.delete_table('dm1_questionnaire_ethnicorigin')

        # Deleting model 'ClinicalTrials'
        db.delete_table('dm1_questionnaire_clinicaltrials')


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
            'gor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'miscarriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obgyn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pneumonia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'pneumoniaage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pneumoniainfections': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'psychological': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sexual_dysfunction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'dm1_questionnaire.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
            'echocardiogram_lvef_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6'})
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
