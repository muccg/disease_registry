# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Diagnosis'
        db.create_table('dm1_diagnosis', (
            ('diagnosis', self.gf('django.db.models.fields.CharField')(default='DM1', max_length=3)),
            ('affectedstatus', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_symptom', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('first_suspected_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('age_at_clinical_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('age_at_molecular_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['patients.Patient'], unique=True, primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dm1', ['Diagnosis'])

        # Adding model 'MotorFunction'
        db.create_table('dm1_motorfunction', (
            ('walk', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('walk_assisted', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('walk_assisted_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('best_function', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('wheelchair_use', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('wheelchair_usage_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dysarthria', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['MotorFunction'])

        # Adding model 'Surgery'
        db.create_table('dm1_surgery', (
            ('cardiac_implant', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('cardiac_implant_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cataract_diagnosis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cataract', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('cataract_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['Surgery'])

        # Adding model 'Heart'
        db.create_table('dm1_heart', (
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=14, null=True, blank=True)),
            ('age_at_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('racing', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('palpitations', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('fainting', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('ecg', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('ecg_sinus_rhythm', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('ecg_pr_interval', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ecg_qrs_duration', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ecg_examination_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('echocardiogram', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('echocardiogram_lvef', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('echocardiogram_lvef_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['Heart'])

        # Adding model 'HeartMedication'
        db.create_table('dm1_heartmedication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1.Diagnosis'])),
        ))
        db.send_create_signal('dm1', ['HeartMedication'])

        # Adding model 'Muscle'
        db.create_table('dm1_muscle', (
            ('myotonia', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
            ('flexor_digitorum_profundis', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('tibialis_anterior', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('neck_flexion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('iliopsoas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=1, blank=True)),
            ('face', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('early_weakness', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal('dm1', ['Muscle'])

        # Adding model 'MuscleMedication'
        db.create_table('dm1_musclemedication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1.Diagnosis'])),
        ))
        db.send_create_signal('dm1', ['MuscleMedication'])

        # Adding model 'Respiratory'
        db.create_table('dm1_respiratory', (
            ('non_invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('age_non_invasive_ventilation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('non_invasive_ventilation_type', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('fvc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('fvc_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('calculatedfvc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['Respiratory'])

        # Adding model 'FeedingFunction'
        db.create_table('dm1_feedingfunction', (
            ('dysphagia', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('gastric_nasal_tube', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['FeedingFunction'])

        # Adding model 'Fatigue'
        db.create_table('dm1_fatigue', (
            ('fatigue', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('sitting_reading', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('watching_tv', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_inactive_public', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('passenger_car', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lying_down_afternoon', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_talking', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_quietly_lunch', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('in_car', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['Fatigue'])

        # Adding model 'FatigueMedication'
        db.create_table('dm1_fatiguemedication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1.Diagnosis'])),
        ))
        db.send_create_signal('dm1', ['FatigueMedication'])

        # Adding model 'SocioeconomicFactors'
        db.create_table('dm1_socioeconomicfactors', (
            ('education', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('employment_effect', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['SocioeconomicFactors'])

        # Adding model 'GeneralMedicalFactors'
        db.create_table('dm1_generalmedicalfactors', (
            ('diabetes', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('diabetesage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pneumonia', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('pneumoniaage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pneumoniainfections', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('cancer', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
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
            ('cognitive_impairment', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('psychological', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('anxiety', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('depression', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apathy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('endocrine', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('obgyn', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medicalert', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('physiotherapy', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('psychologicalcounseling', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('speechtherapy', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('occupationaltherapy', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('vocationaltraining', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['GeneralMedicalFactors'])

        # Adding model 'GeneticTestDetails'
        db.create_table('dm1_genetictestdetails', (
            ('details', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('test_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('laboratory', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('counselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('familycounselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['GeneticTestDetails'])

        # Adding model 'EthnicOrigin'
        db.create_table('dm1_ethnicorigin', (
            ('ethnic_origin', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['EthnicOrigin'])

        # Adding model 'ClinicalTrials'
        db.create_table('dm1_clinicaltrials', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drug_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_sponsor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_phase', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1.Diagnosis'])),
        ))
        db.send_create_signal('dm1', ['ClinicalTrials'])

        # Adding model 'OtherRegistries'
        db.create_table('dm1_otherregistries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1.Diagnosis'])),
            ('registry', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('dm1', ['OtherRegistries'])

        # Adding model 'Notes'
        db.create_table('dm1_notes', (
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('dm1', ['Notes'])

        # Adding model 'FamilyMember'
        db.create_table('dm1_familymember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('family_member_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dm1.Diagnosis'])),
            ('registry_patient', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='dm1_familymember_related', unique=True, null=True, to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dm1', ['FamilyMember'])

        # Adding model 'Consent'
        db.create_table('dm1_consent', (
            ('q1', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('q2', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('q3', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('q4', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('q5', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('q6', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('q7', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('consentdate', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('firstnameparentguardian', self.gf('django.db.models.fields.CharField')(default='', max_length=60, null=True, blank=True)),
            ('lastnameparentguardian', self.gf('django.db.models.fields.CharField')(default='', max_length=60, null=True, blank=True)),
            ('consentdateparentguardian', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('doctor_0', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_0', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_0', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_0', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_1', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_1', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_1', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_1', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_2', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_2', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_2', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_2', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_3', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_3', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_3', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_3', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_4', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_4', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_4', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_4', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_5', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_5', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_5', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_5', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_6', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_6', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_6', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_6', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_7', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_7', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_7', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_7', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_8', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_8', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_8', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_8', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctor_9', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('doctoraddress_9', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
            ('doctortelephone_9', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('specialist_9', self.gf('django.db.models.fields.CharField')(default=None, max_length=60, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dm1.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('dm1', ['Consent'])

        # Adding model 'DiagnosticCategory'
        db.create_table('dm1_diagnosticcategory', (
            ('molecular_data', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['genetic.MolecularData'], unique=True, primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('repeat_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('relative_test', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('relative_ctg_repeat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('relative_cctg_repeat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('dm1', ['DiagnosticCategory'])


    def backwards(self, orm):
        
        # Deleting model 'Diagnosis'
        db.delete_table('dm1_diagnosis')

        # Deleting model 'MotorFunction'
        db.delete_table('dm1_motorfunction')

        # Deleting model 'Surgery'
        db.delete_table('dm1_surgery')

        # Deleting model 'Heart'
        db.delete_table('dm1_heart')

        # Deleting model 'HeartMedication'
        db.delete_table('dm1_heartmedication')

        # Deleting model 'Muscle'
        db.delete_table('dm1_muscle')

        # Deleting model 'MuscleMedication'
        db.delete_table('dm1_musclemedication')

        # Deleting model 'Respiratory'
        db.delete_table('dm1_respiratory')

        # Deleting model 'FeedingFunction'
        db.delete_table('dm1_feedingfunction')

        # Deleting model 'Fatigue'
        db.delete_table('dm1_fatigue')

        # Deleting model 'FatigueMedication'
        db.delete_table('dm1_fatiguemedication')

        # Deleting model 'SocioeconomicFactors'
        db.delete_table('dm1_socioeconomicfactors')

        # Deleting model 'GeneralMedicalFactors'
        db.delete_table('dm1_generalmedicalfactors')

        # Deleting model 'GeneticTestDetails'
        db.delete_table('dm1_genetictestdetails')

        # Deleting model 'EthnicOrigin'
        db.delete_table('dm1_ethnicorigin')

        # Deleting model 'ClinicalTrials'
        db.delete_table('dm1_clinicaltrials')

        # Deleting model 'OtherRegistries'
        db.delete_table('dm1_otherregistries')

        # Deleting model 'Notes'
        db.delete_table('dm1_notes')

        # Deleting model 'FamilyMember'
        db.delete_table('dm1_familymember')

        # Deleting model 'Consent'
        db.delete_table('dm1_consent')

        # Deleting model 'DiagnosticCategory'
        db.delete_table('dm1_diagnosticcategory')


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
            'consentdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'consentdateparentguardian': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'dm1.diagnosis': {
            'Meta': {'ordering': "['patient']", 'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'DM1'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry_patient': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'dm1_familymember_related'", 'unique': 'True', 'null': 'True', 'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
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
            'cancer': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'cancerorgan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancerothers': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancertype': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cholesterol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognitive_impairment': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'constipation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'diabetesage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'dm1.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
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
            'best_function': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'walk': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
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
            'calculatedfvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'dm1.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'dm1.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
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
