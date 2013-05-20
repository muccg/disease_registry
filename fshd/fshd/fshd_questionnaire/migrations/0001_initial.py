# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Patient'
        db.create_table('fshd_questionnaire_patient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('working_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fshd_questionnaire_patient_set', to=orm['groups.WorkingGroup'])),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('given_names', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fshd_questionnaire_patient_set', to=orm['patients.State'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fshd_questionnaire_patient_set', to=orm['patients.Country'])),
            ('postcode', self.gf('django.db.models.fields.IntegerField')()),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Patient'])

        # Adding model 'Diagnosis'
        db.create_table('fshd_questionnaire_diagnosis', (
            ('diagnosis', self.gf('django.db.models.fields.CharField')(default='FSHD', max_length=3)),
            ('affectedstatus', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('first_symptom', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('first_suspected_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('age_at_clinical_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('age_at_molecular_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Patient'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Diagnosis'])

        # Adding model 'MotorFunction'
        db.create_table('fshd_questionnaire_motorfunction', (
            ('walk', self.gf('django.db.models.fields.CharField')(default='', max_length=1)),
            ('walk_assisted', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('walk_assisted_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('best_function', self.gf('django.db.models.fields.CharField')(default='', max_length=8, null=True, blank=True)),
            ('wheelchair_use', self.gf('django.db.models.fields.CharField')(default='', max_length=12)),
            ('wheelchair_usage_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dysarthria', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['MotorFunction'])

        # Adding model 'Surgery'
        db.create_table('fshd_questionnaire_surgery', (
            ('cardiac_implant', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('cardiac_implant_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cataract_diagnosis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cataract', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('cataract_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Surgery'])

        # Adding model 'Heart'
        db.create_table('fshd_questionnaire_heart', (
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
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Heart'])

        # Adding model 'HeartMedication'
        db.create_table('fshd_questionnaire_heartmedication', (
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['HeartMedication'])

        # Adding model 'Respiratory'
        db.create_table('fshd_questionnaire_respiratory', (
            ('non_invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('age_non_invasive_ventilation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('non_invasive_ventilation_type', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('fvc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('fvc_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('calculatedfvc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Respiratory'])

        # Adding model 'Muscle'
        db.create_table('fshd_questionnaire_muscle', (
            ('myotonia', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Muscle'])

        # Adding model 'MuscleMedication'
        db.create_table('fshd_questionnaire_musclemedication', (
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['MuscleMedication'])

        # Adding model 'FeedingFunction'
        db.create_table('fshd_questionnaire_feedingfunction', (
            ('dysphagia', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('gastric_nasal_tube', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['FeedingFunction'])

        # Adding model 'Fatigue'
        db.create_table('fshd_questionnaire_fatigue', (
            ('fatigue', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('sitting_reading', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('watching_tv', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_inactive_public', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('passenger_car', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lying_down_afternoon', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_talking', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sitting_quietly_lunch', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('in_car', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Fatigue'])

        # Adding model 'FatigueMedication'
        db.create_table('fshd_questionnaire_fatiguemedication', (
            ('drug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['FatigueMedication'])

        # Adding model 'SocioeconomicFactors'
        db.create_table('fshd_questionnaire_socioeconomicfactors', (
            ('education', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('employment_effect', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['SocioeconomicFactors'])

        # Adding model 'GeneralMedicalFactors'
        db.create_table('fshd_questionnaire_generalmedicalfactors', (
            ('diabetes', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('diabetesage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pneumonia', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('pneumoniaage', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pneumoniainfections', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('cancer', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
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
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['GeneralMedicalFactors'])

        # Adding M2M table for field cancertype on 'GeneralMedicalFactors'
        db.create_table('fshd_questionnaire_generalmedicalfactors_cancertype', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('generalmedicalfactors', models.ForeignKey(orm['fshd_questionnaire.generalmedicalfactors'], null=False)),
            ('cancertypechoices', models.ForeignKey(orm['fshd.cancertypechoices'], null=False))
        ))
        db.create_unique('fshd_questionnaire_generalmedicalfactors_cancertype', ['generalmedicalfactors_id', 'cancertypechoices_id'])

        # Adding model 'GeneticTestDetails'
        db.create_table('fshd_questionnaire_genetictestdetails', (
            ('details', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('test_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('laboratory', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('counselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('familycounselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['GeneticTestDetails'])

        # Adding model 'EthnicOrigin'
        db.create_table('fshd_questionnaire_ethnicorigin', (
            ('ethnic_origin', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fshd_questionnaire.Diagnosis'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['EthnicOrigin'])

        # Adding model 'ClinicalTrials'
        db.create_table('fshd_questionnaire_clinicaltrials', (
            ('drug_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('trial_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('trial_sponsor', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('trial_phase', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['ClinicalTrials'])

        # Adding model 'Consent'
        db.create_table('fshd_questionnaire_consent', (
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
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['Consent'])

        # Adding model 'FamilyMember'
        db.create_table('fshd_questionnaire_familymember', (
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('family_member_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['FamilyMember'])

        # Adding model 'OtherRegistries'
        db.create_table('fshd_questionnaire_otherregistries', (
            ('registry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fshd_questionnaire.Diagnosis'], primary_key=True)),
        ))
        db.send_create_signal('fshd_questionnaire', ['OtherRegistries'])


    def backwards(self, orm):

        # Deleting model 'Patient'
        db.delete_table('fshd_questionnaire_patient')

        # Deleting model 'Diagnosis'
        db.delete_table('fshd_questionnaire_diagnosis')

        # Deleting model 'MotorFunction'
        db.delete_table('fshd_questionnaire_motorfunction')

        # Deleting model 'Surgery'
        db.delete_table('fshd_questionnaire_surgery')

        # Deleting model 'Heart'
        db.delete_table('fshd_questionnaire_heart')

        # Deleting model 'HeartMedication'
        db.delete_table('fshd_questionnaire_heartmedication')

        # Deleting model 'Respiratory'
        db.delete_table('fshd_questionnaire_respiratory')

        # Deleting model 'Muscle'
        db.delete_table('fshd_questionnaire_muscle')

        # Deleting model 'MuscleMedication'
        db.delete_table('fshd_questionnaire_musclemedication')

        # Deleting model 'FeedingFunction'
        db.delete_table('fshd_questionnaire_feedingfunction')

        # Deleting model 'Fatigue'
        db.delete_table('fshd_questionnaire_fatigue')

        # Deleting model 'FatigueMedication'
        db.delete_table('fshd_questionnaire_fatiguemedication')

        # Deleting model 'SocioeconomicFactors'
        db.delete_table('fshd_questionnaire_socioeconomicfactors')

        # Deleting model 'GeneralMedicalFactors'
        db.delete_table('fshd_questionnaire_generalmedicalfactors')

        # Removing M2M table for field cancertype on 'GeneralMedicalFactors'
        db.delete_table('fshd_questionnaire_generalmedicalfactors_cancertype')

        # Deleting model 'GeneticTestDetails'
        db.delete_table('fshd_questionnaire_genetictestdetails')

        # Deleting model 'EthnicOrigin'
        db.delete_table('fshd_questionnaire_ethnicorigin')

        # Deleting model 'ClinicalTrials'
        db.delete_table('fshd_questionnaire_clinicaltrials')

        # Deleting model 'Consent'
        db.delete_table('fshd_questionnaire_consent')

        # Deleting model 'FamilyMember'
        db.delete_table('fshd_questionnaire_familymember')

        # Deleting model 'OtherRegistries'
        db.delete_table('fshd_questionnaire_otherregistries')


    models = {
        'fshd.cancertypechoices': {
            'Meta': {'object_name': 'CancerTypeChoices'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fshd_questionnaire.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.consent': {
            'Meta': {'object_name': 'Consent'},
            'consentdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'consentdateparentguardian': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
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
        'fshd_questionnaire.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'FSHD'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Patient']", 'unique': 'True', 'primary_key': 'True'})
        },
        'fshd_questionnaire.ethnicorigin': {
            'Meta': {'object_name': 'EthnicOrigin'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.fatigue': {
            'Meta': {'object_name': 'Fatigue'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'fshd_questionnaire.fatiguemedication': {
            'Meta': {'object_name': 'FatigueMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'fshd_questionnaire.feedingfunction': {
            'Meta': {'object_name': 'FeedingFunction'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysphagia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'gastric_nasal_tube': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.generalmedicalfactors': {
            'Meta': {'object_name': 'GeneralMedicalFactors'},
            'anxiety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apathy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cancer': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'cancerorgan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancerothers': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cancertype': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'fshdquestcancertypechoices'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['fshd.CancerTypeChoices']"}),
            'cholesterol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognitive_impairment': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'constipation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'diabetesage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'fshd_questionnaire.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
        'fshd_questionnaire.heartmedication': {
            'Meta': {'object_name': 'HeartMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'fshd_questionnaire.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'best_function': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'walk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'walk_assisted_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12'})
        },
        'fshd_questionnaire.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.musclemedication': {
            'Meta': {'object_name': 'MuscleMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'fshd_questionnaire.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'object_name': 'Patient'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fshd_questionnaire_patient_set'", 'to': "orm['patients.Country']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fshd_questionnaire_patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fshd_questionnaire_patient_set'", 'to': "orm['groups.WorkingGroup']"})
        },
        'fshd_questionnaire.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'age_non_invasive_ventilation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calculatedfvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'fshd_questionnaire.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cardiac_implant_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'cataract_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract_diagnosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fshd_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'})
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

    complete_apps = ['fshd_questionnaire']
