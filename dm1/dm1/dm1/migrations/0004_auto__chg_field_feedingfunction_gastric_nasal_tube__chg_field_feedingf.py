# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FeedingFunction.gastric_nasal_tube'
        db.alter_column('dm1_feedingfunction', 'gastric_nasal_tube', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'FeedingFunction.dysphagia'
        db.alter_column('dm1_feedingfunction', 'dysphagia', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'FamilyMember.relationship'
        db.alter_column('dm1_familymember', 'relationship', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'FamilyMember.sex'
        db.alter_column('dm1_familymember', 'sex', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'FamilyMember.family_member_diagnosis'
        db.alter_column('dm1_familymember', 'family_member_diagnosis', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'GeneticTestDetails.counselling'
        db.alter_column('dm1_genetictestdetails', 'counselling', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'GeneticTestDetails.laboratory'
        db.alter_column('dm1_genetictestdetails', 'laboratory', self.gf('django.db.models.fields.CharField')(default='', max_length=256))

        # Changing field 'GeneticTestDetails.familycounselling'
        db.alter_column('dm1_genetictestdetails', 'familycounselling', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'SocioeconomicFactors.occupation'
        db.alter_column('dm1_socioeconomicfactors', 'occupation', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'SocioeconomicFactors.education'
        db.alter_column('dm1_socioeconomicfactors', 'education', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'SocioeconomicFactors.comments'
        db.alter_column('dm1_socioeconomicfactors', 'comments', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'SocioeconomicFactors.employment_effect'
        db.alter_column('dm1_socioeconomicfactors', 'employment_effect', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'Respiratory.non_invasive_ventilation_type'
        db.alter_column('dm1_respiratory', 'non_invasive_ventilation_type', self.gf('django.db.models.fields.CharField')(default='', max_length=5))

        # Changing field 'Respiratory.non_invasive_ventilation'
        db.alter_column('dm1_respiratory', 'non_invasive_ventilation', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'Respiratory.invasive_ventilation'
        db.alter_column('dm1_respiratory', 'invasive_ventilation', self.gf('django.db.models.fields.CharField')(default='', max_length=2))

        # Changing field 'Heart.ecg'
        db.alter_column('dm1_heart', 'ecg', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Heart.ecg_sinus_rhythm'
        db.alter_column('dm1_heart', 'ecg_sinus_rhythm', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Heart.echocardiogram'
        db.alter_column('dm1_heart', 'echocardiogram', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Heart.palpitations'
        db.alter_column('dm1_heart', 'palpitations', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Heart.fainting'
        db.alter_column('dm1_heart', 'fainting', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Heart.racing'
        db.alter_column('dm1_heart', 'racing', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Heart.condition'
        db.alter_column('dm1_heart', 'condition', self.gf('django.db.models.fields.CharField')(default='', max_length=14))

        # Changing field 'OtherRegistries.registry'
        db.alter_column('dm1_otherregistries', 'registry', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Surgery.cardiac_implant'
        db.alter_column('dm1_surgery', 'cardiac_implant', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'Surgery.cataract'
        db.alter_column('dm1_surgery', 'cataract', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'GeneralMedicalFactors.medicalert'
        db.alter_column('dm1_generalmedicalfactors', 'medicalert', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'GeneralMedicalFactors.occupationaltherapy'
        db.alter_column('dm1_generalmedicalfactors', 'occupationaltherapy', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'GeneralMedicalFactors.cancer'
        db.alter_column('dm1_generalmedicalfactors', 'cancer', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'GeneralMedicalFactors.pneumonia'
        db.alter_column('dm1_generalmedicalfactors', 'pneumonia', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'GeneralMedicalFactors.cancerothers'
        db.alter_column('dm1_generalmedicalfactors', 'cancerothers', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'GeneralMedicalFactors.vocationaltraining'
        db.alter_column('dm1_generalmedicalfactors', 'vocationaltraining', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'GeneralMedicalFactors.pneumoniainfections'
        db.alter_column('dm1_generalmedicalfactors', 'pneumoniainfections', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'GeneralMedicalFactors.cognitive_impairment'
        db.alter_column('dm1_generalmedicalfactors', 'cognitive_impairment', self.gf('django.db.models.fields.CharField')(default='', max_length=6))

        # Changing field 'GeneralMedicalFactors.diabetes'
        db.alter_column('dm1_generalmedicalfactors', 'diabetes', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'GeneralMedicalFactors.cancerorgan'
        db.alter_column('dm1_generalmedicalfactors', 'cancerorgan', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'GeneralMedicalFactors.psychologicalcounseling'
        db.alter_column('dm1_generalmedicalfactors', 'psychologicalcounseling', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'GeneralMedicalFactors.physiotherapy'
        db.alter_column('dm1_generalmedicalfactors', 'physiotherapy', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'GeneralMedicalFactors.speechtherapy'
        db.alter_column('dm1_generalmedicalfactors', 'speechtherapy', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'EthnicOrigin.ethnic_origin'
        db.alter_column('dm1_ethnicorigin', 'ethnic_origin', self.gf('django.db.models.fields.CharField')(default='', max_length=9))

        # Changing field 'Diagnosis.first_symptom'
        db.alter_column('dm1_diagnosis', 'first_symptom', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Diagnosis.first_suspected_by'
        db.alter_column('dm1_diagnosis', 'first_suspected_by', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Consent.firstnameparentguardian'
        db.alter_column('dm1_consent', 'firstnameparentguardian', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Consent.lastnameparentguardian'
        db.alter_column('dm1_consent', 'lastnameparentguardian', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Consent.specialist_2'
        db.alter_column('dm1_consent', 'specialist_2', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_3'
        db.alter_column('dm1_consent', 'specialist_3', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.q1'
        db.alter_column('dm1_consent', 'q1', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.q3'
        db.alter_column('dm1_consent', 'q3', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.q2'
        db.alter_column('dm1_consent', 'q2', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.q5'
        db.alter_column('dm1_consent', 'q5', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.q4'
        db.alter_column('dm1_consent', 'q4', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.q7'
        db.alter_column('dm1_consent', 'q7', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.q6'
        db.alter_column('dm1_consent', 'q6', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Consent.doctoraddress_5'
        db.alter_column('dm1_consent', 'doctoraddress_5', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_4'
        db.alter_column('dm1_consent', 'doctoraddress_4', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_7'
        db.alter_column('dm1_consent', 'doctoraddress_7', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_6'
        db.alter_column('dm1_consent', 'doctoraddress_6', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_1'
        db.alter_column('dm1_consent', 'doctoraddress_1', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_0'
        db.alter_column('dm1_consent', 'doctoraddress_0', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_3'
        db.alter_column('dm1_consent', 'doctoraddress_3', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_2'
        db.alter_column('dm1_consent', 'doctoraddress_2', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_9'
        db.alter_column('dm1_consent', 'doctoraddress_9', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.doctoraddress_8'
        db.alter_column('dm1_consent', 'doctoraddress_8', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Consent.specialist_6'
        db.alter_column('dm1_consent', 'specialist_6', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_7'
        db.alter_column('dm1_consent', 'specialist_7', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_4'
        db.alter_column('dm1_consent', 'specialist_4', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_5'
        db.alter_column('dm1_consent', 'specialist_5', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_8'
        db.alter_column('dm1_consent', 'doctor_8', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_9'
        db.alter_column('dm1_consent', 'doctor_9', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_0'
        db.alter_column('dm1_consent', 'specialist_0', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_1'
        db.alter_column('dm1_consent', 'specialist_1', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_4'
        db.alter_column('dm1_consent', 'doctor_4', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_5'
        db.alter_column('dm1_consent', 'doctor_5', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_6'
        db.alter_column('dm1_consent', 'doctor_6', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_7'
        db.alter_column('dm1_consent', 'doctor_7', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_0'
        db.alter_column('dm1_consent', 'doctor_0', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_1'
        db.alter_column('dm1_consent', 'doctor_1', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_2'
        db.alter_column('dm1_consent', 'doctor_2', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctor_3'
        db.alter_column('dm1_consent', 'doctor_3', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_8'
        db.alter_column('dm1_consent', 'specialist_8', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.specialist_9'
        db.alter_column('dm1_consent', 'specialist_9', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Consent.doctortelephone_9'
        db.alter_column('dm1_consent', 'doctortelephone_9', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_8'
        db.alter_column('dm1_consent', 'doctortelephone_8', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_3'
        db.alter_column('dm1_consent', 'doctortelephone_3', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_2'
        db.alter_column('dm1_consent', 'doctortelephone_2', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_1'
        db.alter_column('dm1_consent', 'doctortelephone_1', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_0'
        db.alter_column('dm1_consent', 'doctortelephone_0', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_7'
        db.alter_column('dm1_consent', 'doctortelephone_7', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_6'
        db.alter_column('dm1_consent', 'doctortelephone_6', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_5'
        db.alter_column('dm1_consent', 'doctortelephone_5', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Consent.doctortelephone_4'
        db.alter_column('dm1_consent', 'doctortelephone_4', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Fatigue.fatigue'
        db.alter_column('dm1_fatigue', 'fatigue', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'MotorFunction.best_function'
        db.alter_column('dm1_motorfunction', 'best_function', self.gf('django.db.models.fields.CharField')(max_length=8))

        # Changing field 'ClinicalTrials.trial_phase'
        db.alter_column('dm1_clinicaltrials', 'trial_phase', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'ClinicalTrials.drug_name'
        db.alter_column('dm1_clinicaltrials', 'drug_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'ClinicalTrials.trial_sponsor'
        db.alter_column('dm1_clinicaltrials', 'trial_sponsor', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'ClinicalTrials.trial_name'
        db.alter_column('dm1_clinicaltrials', 'trial_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Muscle.myotonia'
        db.alter_column('dm1_muscle', 'myotonia', self.gf('django.db.models.fields.CharField')(default='', max_length=6))

        # Changing field 'Muscle.early_weakness'
        db.alter_column('dm1_muscle', 'early_weakness', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Muscle.face'
        db.alter_column('dm1_muscle', 'face', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

    def backwards(self, orm):

        # Changing field 'FeedingFunction.gastric_nasal_tube'
        db.alter_column('dm1_feedingfunction', 'gastric_nasal_tube', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'FeedingFunction.dysphagia'
        db.alter_column('dm1_feedingfunction', 'dysphagia', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'FamilyMember.relationship'
        db.alter_column('dm1_familymember', 'relationship', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'FamilyMember.sex'
        db.alter_column('dm1_familymember', 'sex', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'FamilyMember.family_member_diagnosis'
        db.alter_column('dm1_familymember', 'family_member_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'GeneticTestDetails.counselling'
        db.alter_column('dm1_genetictestdetails', 'counselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneticTestDetails.laboratory'
        db.alter_column('dm1_genetictestdetails', 'laboratory', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'GeneticTestDetails.familycounselling'
        db.alter_column('dm1_genetictestdetails', 'familycounselling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'SocioeconomicFactors.occupation'
        db.alter_column('dm1_socioeconomicfactors', 'occupation', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'SocioeconomicFactors.education'
        db.alter_column('dm1_socioeconomicfactors', 'education', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'SocioeconomicFactors.comments'
        db.alter_column('dm1_socioeconomicfactors', 'comments', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'SocioeconomicFactors.employment_effect'
        db.alter_column('dm1_socioeconomicfactors', 'employment_effect', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Respiratory.non_invasive_ventilation_type'
        db.alter_column('dm1_respiratory', 'non_invasive_ventilation_type', self.gf('django.db.models.fields.CharField')(max_length=5, null=True))

        # Changing field 'Respiratory.non_invasive_ventilation'
        db.alter_column('dm1_respiratory', 'non_invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Respiratory.invasive_ventilation'
        db.alter_column('dm1_respiratory', 'invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Heart.ecg'
        db.alter_column('dm1_heart', 'ecg', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Heart.ecg_sinus_rhythm'
        db.alter_column('dm1_heart', 'ecg_sinus_rhythm', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Heart.echocardiogram'
        db.alter_column('dm1_heart', 'echocardiogram', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Heart.palpitations'
        db.alter_column('dm1_heart', 'palpitations', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Heart.fainting'
        db.alter_column('dm1_heart', 'fainting', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Heart.racing'
        db.alter_column('dm1_heart', 'racing', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Heart.condition'
        db.alter_column('dm1_heart', 'condition', self.gf('django.db.models.fields.CharField')(max_length=14, null=True))

        # Changing field 'OtherRegistries.registry'
        db.alter_column('dm1_otherregistries', 'registry', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Surgery.cardiac_implant'
        db.alter_column('dm1_surgery', 'cardiac_implant', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Surgery.cataract'
        db.alter_column('dm1_surgery', 'cataract', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneralMedicalFactors.medicalert'
        db.alter_column('dm1_generalmedicalfactors', 'medicalert', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneralMedicalFactors.occupationaltherapy'
        db.alter_column('dm1_generalmedicalfactors', 'occupationaltherapy', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneralMedicalFactors.cancer'
        db.alter_column('dm1_generalmedicalfactors', 'cancer', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'GeneralMedicalFactors.pneumonia'
        db.alter_column('dm1_generalmedicalfactors', 'pneumonia', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'GeneralMedicalFactors.cancerothers'
        db.alter_column('dm1_generalmedicalfactors', 'cancerothers', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'GeneralMedicalFactors.vocationaltraining'
        db.alter_column('dm1_generalmedicalfactors', 'vocationaltraining', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneralMedicalFactors.pneumoniainfections'
        db.alter_column('dm1_generalmedicalfactors', 'pneumoniainfections', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'GeneralMedicalFactors.cognitive_impairment'
        db.alter_column('dm1_generalmedicalfactors', 'cognitive_impairment', self.gf('django.db.models.fields.CharField')(max_length=6, null=True))

        # Changing field 'GeneralMedicalFactors.diabetes'
        db.alter_column('dm1_generalmedicalfactors', 'diabetes', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'GeneralMedicalFactors.cancerorgan'
        db.alter_column('dm1_generalmedicalfactors', 'cancerorgan', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'GeneralMedicalFactors.psychologicalcounseling'
        db.alter_column('dm1_generalmedicalfactors', 'psychologicalcounseling', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneralMedicalFactors.physiotherapy'
        db.alter_column('dm1_generalmedicalfactors', 'physiotherapy', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'GeneralMedicalFactors.speechtherapy'
        db.alter_column('dm1_generalmedicalfactors', 'speechtherapy', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'EthnicOrigin.ethnic_origin'
        db.alter_column('dm1_ethnicorigin', 'ethnic_origin', self.gf('django.db.models.fields.CharField')(max_length=9, null=True))

        # Changing field 'Diagnosis.first_symptom'
        db.alter_column('dm1_diagnosis', 'first_symptom', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Diagnosis.first_suspected_by'
        db.alter_column('dm1_diagnosis', 'first_suspected_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Consent.firstnameparentguardian'
        db.alter_column('dm1_consent', 'firstnameparentguardian', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.lastnameparentguardian'
        db.alter_column('dm1_consent', 'lastnameparentguardian', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_2'
        db.alter_column('dm1_consent', 'specialist_2', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_3'
        db.alter_column('dm1_consent', 'specialist_3', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.q1'
        db.alter_column('dm1_consent', 'q1', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.q3'
        db.alter_column('dm1_consent', 'q3', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.q2'
        db.alter_column('dm1_consent', 'q2', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.q5'
        db.alter_column('dm1_consent', 'q5', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.q4'
        db.alter_column('dm1_consent', 'q4', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.q7'
        db.alter_column('dm1_consent', 'q7', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.q6'
        db.alter_column('dm1_consent', 'q6', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Consent.doctoraddress_5'
        db.alter_column('dm1_consent', 'doctoraddress_5', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_4'
        db.alter_column('dm1_consent', 'doctoraddress_4', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_7'
        db.alter_column('dm1_consent', 'doctoraddress_7', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_6'
        db.alter_column('dm1_consent', 'doctoraddress_6', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_1'
        db.alter_column('dm1_consent', 'doctoraddress_1', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_0'
        db.alter_column('dm1_consent', 'doctoraddress_0', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_3'
        db.alter_column('dm1_consent', 'doctoraddress_3', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_2'
        db.alter_column('dm1_consent', 'doctoraddress_2', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_9'
        db.alter_column('dm1_consent', 'doctoraddress_9', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.doctoraddress_8'
        db.alter_column('dm1_consent', 'doctoraddress_8', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Consent.specialist_6'
        db.alter_column('dm1_consent', 'specialist_6', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_7'
        db.alter_column('dm1_consent', 'specialist_7', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_4'
        db.alter_column('dm1_consent', 'specialist_4', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_5'
        db.alter_column('dm1_consent', 'specialist_5', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_8'
        db.alter_column('dm1_consent', 'doctor_8', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_9'
        db.alter_column('dm1_consent', 'doctor_9', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_0'
        db.alter_column('dm1_consent', 'specialist_0', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_1'
        db.alter_column('dm1_consent', 'specialist_1', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_4'
        db.alter_column('dm1_consent', 'doctor_4', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_5'
        db.alter_column('dm1_consent', 'doctor_5', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_6'
        db.alter_column('dm1_consent', 'doctor_6', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_7'
        db.alter_column('dm1_consent', 'doctor_7', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_0'
        db.alter_column('dm1_consent', 'doctor_0', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_1'
        db.alter_column('dm1_consent', 'doctor_1', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_2'
        db.alter_column('dm1_consent', 'doctor_2', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctor_3'
        db.alter_column('dm1_consent', 'doctor_3', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_8'
        db.alter_column('dm1_consent', 'specialist_8', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.specialist_9'
        db.alter_column('dm1_consent', 'specialist_9', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Consent.doctortelephone_9'
        db.alter_column('dm1_consent', 'doctortelephone_9', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_8'
        db.alter_column('dm1_consent', 'doctortelephone_8', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_3'
        db.alter_column('dm1_consent', 'doctortelephone_3', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_2'
        db.alter_column('dm1_consent', 'doctortelephone_2', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_1'
        db.alter_column('dm1_consent', 'doctortelephone_1', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_0'
        db.alter_column('dm1_consent', 'doctortelephone_0', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_7'
        db.alter_column('dm1_consent', 'doctortelephone_7', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_6'
        db.alter_column('dm1_consent', 'doctortelephone_6', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_5'
        db.alter_column('dm1_consent', 'doctortelephone_5', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Consent.doctortelephone_4'
        db.alter_column('dm1_consent', 'doctortelephone_4', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Fatigue.fatigue'
        db.alter_column('dm1_fatigue', 'fatigue', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'MotorFunction.best_function'
        db.alter_column('dm1_motorfunction', 'best_function', self.gf('django.db.models.fields.CharField')(max_length=8, null=True))

        # Changing field 'ClinicalTrials.trial_phase'
        db.alter_column('dm1_clinicaltrials', 'trial_phase', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'ClinicalTrials.drug_name'
        db.alter_column('dm1_clinicaltrials', 'drug_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'ClinicalTrials.trial_sponsor'
        db.alter_column('dm1_clinicaltrials', 'trial_sponsor', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'ClinicalTrials.trial_name'
        db.alter_column('dm1_clinicaltrials', 'trial_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Muscle.myotonia'
        db.alter_column('dm1_muscle', 'myotonia', self.gf('django.db.models.fields.CharField')(max_length=6, null=True))

        # Changing field 'Muscle.early_weakness'
        db.alter_column('dm1_muscle', 'early_weakness', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Muscle.face'
        db.alter_column('dm1_muscle', 'face', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

    models = {
        'dm1.cancertypechoices': {
            'Meta': {'ordering': "['description']", 'object_name': 'CancerTypeChoices'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dm1.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'dm1.consent': {
            'Meta': {'object_name': 'Consent'},
            'consentdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'consentdateparentguardian': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'doctor_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctoraddress_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctortelephone_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'firstnameparentguardian': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'lastnameparentguardian': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'q1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q6': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q7': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'specialist_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'})
        },
        'dm1.diagnosis': {
            'Meta': {'ordering': "['patient']", 'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'DM1'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['patients.Patient']"}),
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
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'})
        },
        'dm1.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1.Diagnosis']"}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry_patient': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'dm1_familymember_related'", 'unique': 'True', 'null': 'True', 'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'dm1.fatigue': {
            'Meta': {'object_name': 'Fatigue'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fatigue': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
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
            'dysphagia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'gastric_nasal_tube': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'dm1.generalmedicalfactors': {
            'Meta': {'object_name': 'GeneralMedicalFactors'},
            'anxiety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apathy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cancer': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'cancerorgan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cancerothers': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cancertype': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dm1cancertypechoices'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['dm1.CancerTypeChoices']"}),
            'cholesterol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognitive_impairment': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'constipation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'diabetesage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'dm1.diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['dm1.Diagnosis']"}),
            'endocrine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gall_bladder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medicalert': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'miscarriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obgyn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupationaltherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'physiotherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'pneumonia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'pneumoniaage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pneumoniainfections': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'psychological': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'psychologicalcounseling': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'sexual_dysfunction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speechtherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'vocationaltraining': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ecg': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ecg_examination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_pr_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_qrs_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_sinus_rhythm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'echocardiogram': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'echocardiogram_lvef': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'echocardiogram_lvef_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fainting': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'palpitations': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'racing': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
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
            'best_function': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'walk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'walk_assisted_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12'})
        },
        'dm1.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'early_weakness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'face': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'flexor_digitorum_profundis': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'iliopsoas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
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
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'dm1.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'age_non_invasive_ventilation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calculatedfvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'dm1.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'dm1.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cardiac_implant_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
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
            'Meta': {'ordering': "['family_name']", 'object_name': 'Doctor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surgery_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'patients.nextofkinrelationship': {
            'Meta': {'object_name': 'NextOfKinRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'patients.parent': {
            'Meta': {'object_name': 'Parent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_date_of_migration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'parent_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'patients.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'unique_together': "(('family_name', 'given_names', 'working_group'),)", 'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consent_form': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'date_of_migration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Doctor']", 'through': "orm['patients.PatientDoctor']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactive_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'next_of_kin_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'next_of_kin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'next_of_kin_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'next_of_kin_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'next_of_kin_home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'next_of_kin_mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'next_of_kin_postcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'next_of_kin_relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.NextOfKinRelationship']", 'null': 'True', 'blank': 'True'}),
            'next_of_kin_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'next_of_kin_set'", 'null': 'True', 'to': "orm['patients.State']"}),
            'next_of_kin_suburb': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'next_of_kin_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Parent']", 'through': "orm['patients.PatientParent']", 'symmetrical': 'False'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'umrn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.WorkingGroup']"})
        },
        'patients.patientdoctor': {
            'Meta': {'object_name': 'PatientDoctor'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Doctor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'patients.patientparent': {
            'Meta': {'object_name': 'PatientParent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Parent']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dm1']